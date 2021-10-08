from datetime import date
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QDate
from UI.app_ui import Ui_MainWindow
from data import json_script, db_script

#Setup UI
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


saved_data = json_script.return_data()
usn = None
intel_search = None
categories = None

def run_app():
    #if no login is saved
    print(MainWindow.size())
    if not saved_data["usn"]:
        ui.apply_style("dark")  #deafult style before login
        MainWindow.showMaximized()
        sys.exit(app.exec_())
    #if login data exist
    else:
        if saved_data["isTemp"]:
            json_script.clear_data()

        global usn, intel_search, categories
        usn = saved_data["usn"]
        intel_search = saved_data["intel_search"]
        categories = saved_data["categories"]

        setup_preferences(categories, saved_data["theme"], saved_data["saveLoginDuration"], intel_search)
        ui.welcome_label.setText(f"Welcome {usn}")

        ui.stackedWidget.setCurrentIndex(1)
        #show the program
        MainWindow.showMaximized()
        sys.exit(app.exec_())

def setup_preferences(categories, theme, saveLogin, intel_search):
    ui.apply_style(theme)
    ui.add_category_comboBox.addItems(categories.split(","))
    (ui.light_radioButton_3, ui.dark_radioButton_3)[{"light":0, "dark":1}[theme]].setChecked(True)
    (ui.forever_remember_radioButton, ui.year_remember_radioButton, ui.month_remember_radioButton, ui.week_remember_radioButton, ui.day_remember_radioButton, ui.never_remember_radioButton)[{"never": 5, "1day": 4, "1week": 3, "1month": 2, "1year": 1, "forever": 0}[saveLogin]].setChecked(True)
    (ui.light_radioButton_4, ui.dark_radioButton_4)[{"True":0, "False":1}[intel_search]].setChecked(True)
#--------------Login/Signup---------------#
from scripts import login

def toggle_login_signup():
    #clear lineEdits and feedbacks
    index = 1 if ui.login_signup_stackedWidget.currentIndex() == 0 else 0
    for elem in ((ui.login_username_lineEdit, ui.login_password_lineEdit, ui.login_feedback_label), (ui.signup_username_lineEdit, ui.signup_password_lineEdit, ui.signup_password_lineEdit_2, ui.signup_email_lineEdit, ui.signup_feedback_label))[index]:
        elem.clear()
    #change the index of the stackedWidget(change the shown page)
    ui.login_signup_stackedWidget.setCurrentIndex(index)

ui.switch_to_login_pushButton.clicked.connect(toggle_login_signup)
ui.switch_to_signup_pushButton.clicked.connect(toggle_login_signup)

def try_login():
    respond = login.login(ui.login_username_lineEdit.text(), ui.login_password_lineEdit.text(), ui.remember_me_checkBox.isChecked())
    if respond[0]:
        setup_preferences(*respond[1][1:])            
        
        global usn, intel_search, categories
        usn = respond[1][0]
        intel_search = respond[1][-1]
        categories = respond[1][1]

        ui.welcome_label.setText(f"Welcome {usn}")

        ui.stackedWidget.setCurrentIndex(1)

        #click light theme radioButton to apply light theme
        if respond[1][2] == "light":
            ui.light_radioButton_3.click()

    else:
        ui.login_feedback_label.setText(respond[1])

def try_signup():
    respond = login.signup(ui.signup_username_lineEdit.text(), ui.signup_password_lineEdit.text(), ui.signup_password_lineEdit_2.text(), ui.signup_email_lineEdit.text())
    if respond[0]:
        ui.switch_to_login_pushButton.click()
    else:
        ui.signup_feedback_label.setText(respond[1])

def logout():
    import os
    json_script.clear_data()
    #restart the program
    os.execl(sys.executable, 'python', 'main.py', *sys.argv)

ui.login_pushButton.clicked.connect(try_login)
ui.signup_pushButton.clicked.connect(try_signup)
ui.signout_pushButton.clicked.connect(logout)

#--------------Left menu buttons---------------#
btnOnFocusIndex = 0
def switch_page(index):
    global btnOnFocusIndex
    left_menu_btns = [ui.go_search_pushButton, ui.go_add_pushButton, ui.go_control_pushButton, ui.go_settings_pushButton]
    #reset focused btn style
    left_menu_btns[btnOnFocusIndex].setStyleSheet("""
    QPushButton{
	    background-color: rgb(18, 18, 18);
	    border: 2px solid rgb(18, 18, 18);
	}
	QPushButton:hover{
	    background-color: rgb(212, 212, 212);
	    border: 2px solid rgb(212, 212, 212);
	}
    """)
    #change the current chown page
    ui.app_stackedWidget.setCurrentIndex(index)
    #set focus style to the clicked button
    left_menu_btns[index].setStyleSheet("""
    QPushButton{
	    background-color: rgb(75, 75, 75);
	    border: 2px solid rgb(75, 75, 75);
	}
	QPushButton:hover{
	    background-color: rgb(212, 212, 212);
	    border: 2px solid rgb(212, 212, 212);
	}
    """)
    #change current focused btn index
    btnOnFocusIndex = index

#setup left-menu buttons
ui.go_search_pushButton.clicked.connect(lambda: switch_page(0))
ui.go_add_pushButton.clicked.connect(lambda: switch_page(1))
ui.go_control_pushButton.clicked.connect(lambda: switch_page(2))
ui.go_settings_pushButton.clicked.connect(lambda: switch_page(3))

#apply focus style on search button
ui.go_search_pushButton.click()


#--------------Search---------------#
from scripts import feedback_dialog, helpers
from scripts.Dialogs import more_dialog
from pyperclip import copy  #copy to clipboard


#lineEdits that display differents informations (search results)
search_reslt_lineEdits = (ui.username_lineEdit, ui.email_lineEdit, ui.appName_lineEdit, ui.password_lineEdit, ui.creationDate_lineEdit, ui.category_lineEdit)

#set password lineEdit view to PASSWORD
ui.password_lineEdit.setEchoMode(2)

#disable next/prev buttons
ui.next_pushButton.setDisabled(True)
ui.prev_pushButton.setDisabled(True)

#disable more options buttons
ui.more_pushButton.setDisabled(True)
ui.edit_pushButton.setDisabled(True)
ui.delete_pushButton.setDisabled(True)

search_results = None   #contain all results returned from database
current_result_index = 0    #index of on-display result

#display result of current index
def display_result():
    global search_results, current_result_index
    for item, data in zip(search_reslt_lineEdits, search_results[current_result_index][1:7]):
        item.setText(data)
    #display current index(1 --> ...)
    ui.current_index_lcdNumber.display(current_result_index+1)
    
    #enable/disable previous and next buttons
    #enable [prev]
    if current_result_index > 0:
        ui.prev_pushButton.setDisabled(False)
    #disable [prev]
    else:
        ui.prev_pushButton.setDisabled(True)
    #enable/disable next button
    #enable [next]
    if current_result_index < len(search_results) - 1:
        ui.next_pushButton.setDisabled(False)
    #disable [next]
    else:
        ui.next_pushButton.setDisabled(True)

#clear/reset search page
def clear_search():
    #clear results lineEdits
    for elem in search_reslt_lineEdits:
        elem.clear()
    #clear feedback
    ui.search_feedback.clear()
    #set 0's to results_found and current_index
    ui.results_found_lcdnumber.display(0)
    ui.current_index_lcdNumber.display(0)
    #disable next/prev buttons
    ui.next_pushButton.setDisabled(True)
    ui.prev_pushButton.setDisabled(True)
    #disable more options buttons
    ui.more_pushButton.setDisabled(True)
    ui.edit_pushButton.setDisabled(True)
    ui.delete_pushButton.setDisabled(True)

#main search function
def search():
    #reset page
    clear_search()
    global search_results, current_result_index
    #get search results
    search_query = ui.search_lineEdit.text().strip() if intel_search == "True" else ui.search_lineEdit.text()
    search_results = db_script.search_info(usn, helpers.modify_searchBy(ui.search_by_comboBox.currentText()), search_query, intel_search)
    #if results found
    if search_results:
        current_result_index = 0
        #display nb of founds results
        ui.results_found_lcdnumber.display(len(search_results))
        #enable more options buttons
        ui.more_pushButton.setDisabled(False)
        ui.edit_pushButton.setDisabled(False)
        ui.delete_pushButton.setDisabled(False)
        #display first result
        display_result()
    #if no results found
    else:
        ui.search_feedback.setText("No results found!")

#switch to the next result
def next_search_result():
    global current_result_index
    current_result_index += 1
    display_result()

#switch to the previous result
def previous_search_result():
    global current_result_index
    current_result_index -= 1
    display_result()

#show more informations about current on-display result in more dialog
def open_more():
    MainWindow.hide()
    more_dialog.reset_dialog()
    more_dialog.display_result(search_results[current_result_index][1:])
    more_dialog.run()
    MainWindow.show()

#cancel editing current on-display result
def cancel_editing():
    #reset more button
    ui.more_pushButton.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/more-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.more_pushButton.setIcon(icon)
    ui.more_pushButton.disconnect()     #disconnect edit function (save)
    ui.more_pushButton.clicked.connect(open_more)
    #reset delete button
    ui.delete_pushButton.setText("")
    icon.addPixmap(QtGui.QPixmap("icons/delete_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.delete_pushButton.setIcon(icon)
    ui.delete_pushButton.disconnect()     #disconnect edit function (cancel)
    ui.delete_pushButton.clicked.connect(delete_current_result)
    #enable edit button
    ui.edit_pushButton.setDisabled(False)
    #set linEdits to don't accept edit (read-only)
    for lineEdit in (ui.username_lineEdit, ui.email_lineEdit, ui.appName_lineEdit, ui.password_lineEdit):
        lineEdit.setReadOnly(True)
    #reset display to the saved informations
    display_result()

#edit current on-display result
def edit_current_result():
    #setup save button
    ui.more_pushButton.setText("Save")
    ui.more_pushButton.setIcon(QtGui.QIcon())
    ui.more_pushButton.disconnect()     #disconnect default function (open_more)
    ui.more_pushButton.clicked.connect(save_editing)
    #setup cancel button
    ui.delete_pushButton.setText("Cancel")
    ui.delete_pushButton.setIcon(QtGui.QIcon())
    ui.delete_pushButton.disconnect()       #disconnect default function (delete_current_result)
    ui.delete_pushButton.clicked.connect(cancel_editing)
    #disable edit button
    ui.edit_pushButton.setDisabled(True)
    #set linEdits to accept edit    (read & write)
    for lineEdit in (ui.username_lineEdit, ui.email_lineEdit, ui.appName_lineEdit, ui.password_lineEdit):
        lineEdit.setReadOnly(False)

#helper: check if informations after edit are valid/accepted
def acceptEdit(data_lst):
    #required data entered
    if any(data_lst[ :3]) and data_lst[3]:
        #if email changed
        if data_lst[1] != "-":
            #if email is not valid
            if not helpers.isEmail(data_lst[1]):
                return (False, "Entered E-mail is invalid...")
        #required data entered and email is valid
        return (True, )
    #required data not entered
    return (False, "You must enter at least one of (username, email, app name) and a password...")
    
#apply/save edit
def save_editing():
    #show feedback dialog to get confirmation from user
    feedback_dialog.show_feedback("Are you sure you want to update this informations?\nThis operation can not be undo!")
    #helper var: to know if edit must be closed or stay open
    keepEdit = False
    #if user confirm edit
    if feedback_dialog.feedbackIsConfirmed:
        global current_result_index
        #list store the new data (after edit)
        newData = []
        #get saved lastUpdateDate (from search results)
        lastUpdateDate = search_results[current_result_index][8]
        #save new/editted main informations in newData list
        for lineEdit in (ui.username_lineEdit, ui.email_lineEdit, ui.appName_lineEdit, ui.password_lineEdit):
            newData.append(lineEdit.text())
        #check if password is changed
        if search_results[current_result_index][4] != ui.password_lineEdit.text():
            #if first time update
            if lastUpdateDate == "Never":
                lastUpdateDate = ",".join(["First time", str(date.today())])
            #if there is previous update dates saved
            else:
                #transform saved lastUpdateDate to list
                lastUpdateDate = lastUpdateDate.split(",")
                #add the new date
                lastUpdateDate.append(str(date.today()))
                #retransform to string in the final format (in wich will be saved in database)
                lastUpdateDate = ",".join(lastUpdateDate)
        
        #add lastUpdateDate to the data lst
        newData.append(lastUpdateDate)
        #add password rate
        newData.append(helpers.checkPasswordRate(newData[3]))
        #remove empty
        newData = helpers.removeEmpty(newData)
        #validate changed informations (newData list)
        validation = acceptEdit(newData)
        #if valid
        if validation[0]:
            #save in database
            db_script.update_info(usn, search_results[current_result_index][0], newData)
        #if not valid
        else:
            #show feedback containing the error
            feedback_dialog.show_feedback(validation[1])
            #kepp edit on
            keepEdit = True

    #close edit and apply changes
    if not keepEdit:
        #cancel edit
        cancel_editing()
        #update on-display result
        lastIndex = current_result_index
        search()    #to get updated informations from database
        # display the changed result (!!if searchBy keyword is not changed while editing!!)
        current_result_index = lastIndex
        display_result()

#delete current on-display result
def delete_current_result():
    #show feedback
    feedback_dialog.show_feedback("Are you sure you Want to delete this password?\nYou will not be able to undo!")
    #delete if operation confirmed
    if feedback_dialog.feedbackIsConfirmed:
        db_script.delete_info(usn, search_results[current_result_index][0])
        #get updated informations from database
        search()

#copy to clipboard
def copy_to_clipboard(index):
    copy(search_reslt_lineEdits[index].text().strip())

#toggle password view(normal/hidden)
def toggle_password_view(pswd_lineEdit, pswd_view_toggle_btn):
    pswd_lineEdit.setEchoMode(0 if pswd_lineEdit.echoMode() else 2)
    #change icon
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons\openEye-icon.svg" if pswd_lineEdit.echoMode() else "icons\closedEye-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    pswd_view_toggle_btn.setIcon(icon)


#Setup buttons
ui.search_password_pushButton.clicked.connect(search)
ui.next_pushButton.clicked.connect(next_search_result)
ui.prev_pushButton.clicked.connect(previous_search_result)

ui.more_pushButton.clicked.connect(open_more)
ui.edit_pushButton.clicked.connect(edit_current_result)
ui.delete_pushButton.clicked.connect(delete_current_result)
#setup copy to clipboard buttons
ui.username_copy_pushButton.clicked.connect(lambda : copy_to_clipboard(0))
ui.email_copy_pushButton.clicked.connect(lambda : copy_to_clipboard(1))
ui.password_copy_pushButton.clicked.connect(lambda : copy_to_clipboard(3))
#password view toggle button
ui.password_hide_show_pushButton.clicked.connect(lambda : toggle_password_view(ui.password_lineEdit, ui.password_hide_show_pushButton))
#--------------Add---------------#
from scripts.Dialogs import categories_dialog

main_add_inputs = (ui.add_username_lineEdit, ui.add_email_lineEdit, ui.add_appName_lineEdit, ui.add_password_lineEdit, ui.add_telNb_lineEdit)

#set the date on today
ui.add_creationDate_dateEdit.setDate(QDate(date.today()))
#set the password lineEdit on password view
ui.add_password_lineEdit.setEchoMode(2)

#check if entered email match the email pattern and give the feedback if not            
def checkEmail(email):
    if helpers.isEmail(email) or not email.strip():
        return True
    else:
        ui.add_save_feedback.setText("Invalid E-mail is entered!")
        return False

#check if entered mobile nb match the pattern and give the feedback if not
def checkMobileNb(nb):
    if helpers.isMobileNb(nb) or not nb.strip():
        return True
    else:
        ui.add_save_feedback.setText("Invalid mobile number is entered!")
        return False

#reset add page
def reset_add():
    for elem in main_add_inputs:
        elem.clear()
    ui.add_save_feedback.clear()
    ui.add_note_textEdit.clear()
    ui.add_category_comboBox.setCurrentIndex(0)
    ui.add_creationDate_dateEdit.setDate(QDate(date.today()))
    ui.add_additionalInfo_enable_radioButton.click()

#main save function
def save_info():
    entered_data = [elem.text() for elem in main_add_inputs]
    #check if at least one of (username, email, app name) is entered and password
    if any(entered_data[0:3]) and entered_data[3]:
        #check entered email and tel nb are valid
        if checkEmail(entered_data[1]) and checkMobileNb(entered_data[4]):
            #apply removeEmpty() function on entered data to transform empty strings to "-"
            entered_data = helpers.removeEmpty(entered_data)
            #get optional data (creation date, category, note)
            creationDate = ui.add_creationDate_dateEdit.text() if ui.add_creationDate_dateEdit.isEnabled() else "-"
            category = ui.add_category_comboBox.currentText() if ui.add_category_comboBox.isEnabled() else "-"
            note = ui.add_note_textEdit.toPlainText().strip() if ui.add_note_textEdit.isEnabled() and ui.add_note_textEdit.toPlainText().strip() else "-"
            #check the password rate
            passwordRate = helpers.checkPasswordRate(entered_data[3])
            #order the data in data_lst to enter it as argument to db_script.save_info()
            data_lst = entered_data[0:-1]
            data_lst.extend([creationDate, category, str(date.today()), "Never", entered_data[-1], passwordRate, note])
            #save entered data in database
            db_script.save_info(usn, data_lst)
            #clear all inputs
            reset_add()
            #show "SAVED" feedback
            ui.add_save_feedback.setStyleSheet("color: rgb(0, 255, 100)")
            ui.add_save_feedback.setText("Saved..")

    else:
        ui.add_save_feedback.setStyleSheet("color: rgb(255, 0, 0);")
        ui.add_save_feedback.setText("Please enter at least one of (username, email, app name) and a password.")

#check and update the password rate
def change_rate():
    rate = helpers.checkPasswordRate(ui.add_password_lineEdit.text())
    if rate:
        colors = {"Weak": 'rgb(255, 0, 0)', "OK": 'rgb(0,255,0)', "Good": 'rgb(0, 255, 0)', "Strong": 'rgb(0,0,255)'}
        ui.add_passwordRate_label.setStyleSheet(f"color: {colors[rate]}")
    ui.add_passwordRate_label.setText(f"    {rate}" if rate else "")

#disable and enable the additional info area
def disable_enable_additional_info(enable):
    #Disable
    if not enable:
        for elem in (ui.add_creationDate_enable_disable_pushButton, ui.add_creationDate_dateEdit, ui.add_category_comboBox, ui.A_manage_category_pushButton, ui.add_note_textEdit):
            elem.setDisabled(True)
            if not elem == ui.A_manage_category_pushButton:
                    elem.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0, 0, 0)")
    #Enable
    else:
        for elem in (ui.add_creationDate_enable_disable_pushButton, ui.add_creationDate_dateEdit, ui.add_category_comboBox, ui.A_manage_category_pushButton, ui.add_note_textEdit):
            elem.setDisabled(False)
            if not elem == ui.A_manage_category_pushButton:
                elem.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")

#disable and enable creation date dateEdit
def disable_enable_add_date():
    ui.add_creationDate_dateEdit.setEnabled(False if ui.add_creationDate_dateEdit.isEnabled() else True)
    ui.add_creationDate_dateEdit.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0, 0, 0)" if not ui.add_creationDate_dateEdit.isEnabled() else "background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")

#clear the feedback
def clear_add_feedback():
    ui.add_save_feedback.clear()

#open manage categories dialog
def manage_categories():
    global categories
    categories = categories_dialog.run(usn, categories)
    ui.add_category_comboBox.clear()
    ui.add_category_comboBox.addItems(categories)
    categories = ",".join(categories)

#setup main add buttons
ui.add_save_pushButton.clicked.connect(save_info)
ui.add_clear_pushButton.clicked.connect(reset_add)
ui.add_additionalInfo_disable_radioButton.clicked.connect(lambda : disable_enable_additional_info(False))
ui.add_additionalInfo_enable_radioButton.clicked.connect(lambda : disable_enable_additional_info(True))
ui.add_creationDate_enable_disable_pushButton.clicked.connect(disable_enable_add_date)
ui.add_password_hide_show_pushButton.clicked.connect(lambda : toggle_password_view(ui.add_password_lineEdit, ui.add_password_hide_show_pushButton))

#update password rate when changing password
ui.add_password_lineEdit.textChanged.connect(change_rate)

#clear feedback when entering/changing data
ui.add_username_lineEdit.textChanged.connect(clear_add_feedback)
ui.add_appName_lineEdit.textChanged.connect(clear_add_feedback)
ui.add_email_lineEdit.textChanged.connect(clear_add_feedback)
ui.add_password_lineEdit.textChanged.connect(clear_add_feedback)

#open manage categories
ui.A_manage_category_pushButton.clicked.connect(manage_categories)

#--------------Control Panel---------------#
from scripts.Dialogs import view_dialog, report_dialog, delete_all_dialog

#view all password Dialog
def view_panel():
    MainWindow.hide()
    view_dialog.run_view_dialog(usn)
    MainWindow.show()

#report dialog
def view_report():
    MainWindow.hide()
    report_dialog.run(usn)
    with open("temp_data\selected_id.txt", "r") as f:
        id = f.readline()
        try:
            int(id)
            ui.go_search_pushButton.click()
            ui.search_by_comboBox.setCurrentIndex(4)
            ui.search_lineEdit.setText(id)
            ui.search_password_pushButton.click()
            ui.edit_pushButton.click()
            ui.password_lineEdit.setFocus()
            MainWindow.show()
        except:
            MainWindow.show()

#Clear all data dialog
def start_delete_all():
    MainWindow.hide()
    delete_all_dialog.run(usn)
    MainWindow.show()

ui.view_all_password_commandLinkButton.clicked.connect(view_panel)
ui.report_commandLinkButton.clicked.connect(view_report)
ui.clear_all_password_commandLinkButton.clicked.connect(start_delete_all)

#--------------Settings---------------#
lastBtnIndex = None 
def toggle_settings(index):
    global lastBtnIndex
    ui.settings_pages_stackedWidget.setCurrentIndex(index)
    #set focus style to the clicked button
    btns = (ui.change_password_commandLinkButton_2, ui.account_restore_commandLinkButton_2, ui.password_remember_commandLinkButton_2, ui.history_commandLinkButton_2, ui.delete_account_commandLinkButton_2, ui.about_commandLinkButton)
    btns[index].setDisabled(True)
    #reset last button clicked
    if type(lastBtnIndex) is int:
        btns[lastBtnIndex].setDisabled(False)
    #change last button clicked
    lastBtnIndex = index
    #set title
    ui.settings_page_groupBox.setTitle(ui.settings_titles[index])

#setup toggling buttons
ui.change_password_commandLinkButton_2.clicked.connect(lambda: toggle_settings(0))
ui.account_restore_commandLinkButton_2.clicked.connect(lambda: toggle_settings(1))
#click [change password]
ui.change_password_commandLinkButton_2.click()

#change password----------->

#reset change password page
def reset_change_password():
    ui.change_password_current_password_lineEdit.clear()
    ui.change_password_new_password_lineEdit.clear()
    ui.change_password_new_password_lineEdit_2.clear()
    ui.change_password_feedback.clear()

#main change password function
def change_password():
    from scripts.hash import hash
    if hash(ui.change_password_current_password_lineEdit.text().strip()) == db_script.search_user(usn)[2]:
        if ui.change_password_new_password_lineEdit.text().strip() == ui.change_password_new_password_lineEdit_2.text().strip():
            if len(newPass:= ui.change_password_new_password_lineEdit_2.text().strip()) >= 4 and len(newPass.split()) == 1:
                db_script.change_login_password(usn, hash(newPass))
                ui.change_password_feedback.setStyleSheet("color: rgb(0,255,0)")
                reset_change_password()
                ui.change_password_feedback.setText("Password Successfuly changed...")
            else:
                ui.change_password_feedback.setStyleSheet("color: rgb(255,0,0)")
                ui.change_password_feedback.setText("Password must contains at least 4 characters without spaces!")
        else:
            ui.change_password_feedback.setStyleSheet("color: rgb(255,0,0)")
            ui.change_password_feedback.setText("Entered new passwords are differents!")
    else:
        ui.change_password_feedback.setStyleSheet("color: rgb(255,0,0)")
        ui.change_password_feedback.setText("Invalid current password!")

#setup change password button
ui.change_password_save_pushButton.clicked.connect(change_password)
#clear feedback when changing any entered password
ui.change_password_current_password_lineEdit.textChanged.connect(lambda: ui.change_password_feedback.clear())
ui.change_password_new_password_lineEdit.textChanged.connect(lambda: ui.change_password_feedback.clear())
ui.change_password_new_password_lineEdit_2.textChanged.connect(lambda: ui.change_password_feedback.clear())

#Password remember----------->
ui.password_remember_note_groupBox.hide()

def getCheckedChoice():
    choicesBoxes = (ui.forever_remember_radioButton, ui.year_remember_radioButton, ui.month_remember_radioButton, ui.week_remember_radioButton, ui.day_remember_radioButton, ui.never_remember_radioButton)
    checked = "".join([box.text() for box in choicesBoxes if box.isChecked()][0].split()).lower()
    db_script.change_remember_duration(usn, checked)
    choicesBoxes[{"never": 5, "1day": 4, "1week": 3, "1month": 2, "1year": 1, "forever": 0}[checked]].setChecked(True)
    ui.password_remember_feedback.setText("Change Applied!")
    ui.password_remember_note_groupBox.show()

def reset_password_remember():
    ui.password_remember_note_groupBox.hide()
    ui.password_remember_feedback.clear()

def toggle_password_remember():
    reset_password_remember()
    toggle_settings(2)

ui.password_remember_commandLinkButton_2.clicked.connect(toggle_password_remember)
ui.password_remember_apply_pushButton.clicked.connect(getCheckedChoice)


#History----------->
def show_history():
    ui.login_history_textBrowser.setText(str("\n"+"-"*40+"\n").join(db_script.search_user(usn)[8].split(",")[::-1]))
    toggle_settings(3)

ui.history_commandLinkButton_2.clicked.connect(show_history)

#delete account----------->
ui.delete_account_next_step_pushButton.setDisabled(True)
ui.delete_account_next_step_pushButton_2.setDisabled(True)

def start_delete_account():
    ui.delete_account_steps_stackedWidget.setCurrentIndex(0)
    ui.delete_account_username_lineEdit.clear()
    ui.delete_account_password_lineEdit.clear()
    if not ui.delete_account_next_step_pushButton.isEnabled():
        return toggle_settings(4)
    ui.delete_account_next_step_pushButton.setDisabled(True)
    ui.delete_account_step1_feedback.clear()
    ui.delete_account_next_step_pushButton_2.setDisabled(True)
    ui.delete_account_step2_agree_checkBox.setChecked(False)

#delete account button
ui.delete_account_commandLinkButton_2.clicked.connect(start_delete_account)

        
    #Step 1:
def check_account():
    from scripts.hash import hash
    if ui.delete_account_username_lineEdit.text().strip() == usn:
        #check that entered password is correct
        #print(f"db response: {db_script.search_user(usn)[2]}")
        #print(f"password entered: {hash(ui.delete_account_password_lineEdit.text())}")
        if hash(ui.delete_account_password_lineEdit.text().strip()) == db_script.search_user(usn)[2]:
            #enable next button (to switch to next step)
            ui.delete_account_next_step_pushButton.setDisabled(False)
            #disable username and password lineEdits(to avoid any change after verificaion)
            ui.delete_account_username_lineEdit.setDisabled(True)
            ui.delete_account_password_lineEdit.setDisabled(True)
            #display feedback
            ui.delete_account_step1_feedback.setStyleSheet("color: rgb(0,255,0);")
            ui.delete_account_step1_feedback.setText("Verified... Press next")
            return
    #wrong userename or password
    ui.delete_account_step1_feedback.setStyleSheet("color: rgb(255,0,0);")
    ui.delete_account_step1_feedback.setText("Invalid inputs!")


#step 1 buttons
ui.delete_account_step1_check_pushButton.clicked.connect(check_account)
ui.delete_account_next_step_pushButton.clicked.connect(lambda: ui.delete_account_steps_stackedWidget.setCurrentIndex(1))
#clear feedback when changing username or password
ui.delete_account_username_lineEdit.textChanged.connect(lambda: ui.delete_account_step1_feedback.clear())
ui.delete_account_password_lineEdit.textChanged.connect(lambda: ui.delete_account_step1_feedback.clear())

    #Step 2:
def toggle_next():
    ui.delete_account_next_step_pushButton_2.setDisabled(True if ui.delete_account_next_step_pushButton_2.isEnabled() else False)

ui.delete_account_step2_agree_checkBox.clicked.connect(toggle_next)
ui.delete_account_next_step_pushButton_2.clicked.connect(lambda: ui.delete_account_steps_stackedWidget.setCurrentIndex(2))

    #Step 3:
def check_text():
    if ui.delete_account_specific_text_lineEdit.text() == "Delete account":
        db_script.clear_user(usn)
        ui.signout_pushButton.click()
    else:
        ui.delete_account_specific_text_lineEdit.setStyleSheet("""
        QLineEdit{
            border: 2px solid red;
        }
        """)

def reset_text_lineEdit():
    ui.delete_account_specific_text_lineEdit.setStyleSheet("""
    background-color: rgb(255,255,255);
    color: rgb(0,0,0);
    border: 0;
    """)

ui.delete_account_step3_confirm_pushButton.clicked.connect(check_text)
ui.delete_account_specific_text_lineEdit.textChanged.connect(reset_text_lineEdit)


#toggle intelligence search----------->
import os

def change_intel_search(newChoice):
    db_script.change_intelligence_search(usn, newChoice)
    if saved_data["usn"]:
        dts = [saved_data[k] for k in saved_data.keys()]
        json_script.update_data(dts[0], dts[1], dts[2], dts[3], dts[4], newChoice, dts[6])
    os.execl(sys.executable, 'python', 'main.py', *sys.argv)

ui.dark_radioButton_4.clicked.connect(lambda: change_intel_search("False"))
ui.light_radioButton_4.clicked.connect(lambda: change_intel_search("True"))


#change theme----------->

#change theme in json file if login saved or save data temporary
def change_theme(theme):
    db_script.change_theme(usn, theme)
    current_saved_data = json_script.return_data()
    if current_saved_data["usn"]:
        old_data = current_saved_data
        json_script.update_data(old_data['usn'], theme, old_data['saveLoginDuration'], old_data['categories'], old_data['sessionOpenDate'], old_data["intel_search"], False)
    else:
        db_data = db_script.search_user(usn)
        json_script.clear_data()
        json_script.update_data(usn, theme, "forever", db_data[4], None, db_data[9], True)


def theme_light():
    change_theme('light')
    os.execl(sys.executable, 'python', 'main.py', *sys.argv)

def theme_dark():
    change_theme('dark')
    os.execl(sys.executable, 'python', 'main.py', *sys.argv)

ui.light_radioButton_3.clicked.connect(theme_light)
ui.dark_radioButton_3.clicked.connect(theme_dark)

#about----------------->
ui.about_commandLinkButton.clicked.connect(lambda: toggle_settings(5))
def about_show():
    ...

#RUNNNN
run_app()