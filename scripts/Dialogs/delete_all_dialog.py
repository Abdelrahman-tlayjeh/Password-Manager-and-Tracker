from PyQt5 import QtWidgets
from UI import delete_all_dialog_ui
from data import db_script
from scripts import hash

Dialog = QtWidgets.QDialog()
ui = delete_all_dialog_ui.Ui_Dialog()
ui.setupUi(Dialog)

usn = None

def run(username):
    global usn
    usn = username
    Dialog.exec_()
    reset()

ui.next_step_pushButton.setDisabled(True)
ui.next_step_pushButton_2.setDisabled(True)

def reset():
    global usn
    usn = None
    ui.delete_account_steps_stackedWidget.setCurrentIndex(0)
    ui.username_lineEdit.clear()
    ui.password_lineEdit.clear()
    #if first next button is disabled
    if not ui.next_step_pushButton.isEnabled():
        return
    #reset step 2
    ui.next_step_pushButton.setDisabled(True)
    ui.username_lineEdit.setDisabled(False)
    ui.password_lineEdit.setDisabled(False)
    #if second next button is disabled
    if not ui.next_step_pushButton_2.isEnabled():
        return
    #reset step 3
    ui.next_step_pushButton_2.setDisabled(True)
    ui.step2_agree_checkBox.setChecked(False)
    ui.specific_text_lineEdit.clear()
    ui.specific_text_lineEdit.setDisabled(False)


#step 0--------------->

#start with step 1
def start():
    ui.delete_account_steps_stackedWidget.setCurrentIndex(1)

#close the dialog
def cancel():
    Dialog.close()

#setup buttons
ui.start_pushButton.clicked.connect(start)
ui.cancel_pushButton.clicked.connect(cancel)

#step 1--------------->

#check login (username & password)
def check_account():
    #check that entered username is the same logged in username 
    if ui.username_lineEdit.text().strip() == usn:
        #check that entered password is correct
        if hash.hash(ui.password_lineEdit.text().strip()) == db_script.search_user(usn)[2]:
            #enable next button (to switch to next step)
            ui.next_step_pushButton.setDisabled(False)
            #disable username and password lineEdits(to avoid any change after verificaion)
            ui.username_lineEdit.setDisabled(True)
            ui.password_lineEdit.setDisabled(True)
            #display feedback
            ui.step1_feedback.setStyleSheet("color: rgb(0,255,0);")
            ui.step1_feedback.setText("Verified... Press next")
            return
    #wrong userename or password
    ui.step1_feedback.setStyleSheet("color: rgb(255,0,0);")
    ui.step1_feedback.setText("Invalid inputs!")

#switch to step 2
def go_step2():
    ui.delete_account_steps_stackedWidget.setCurrentIndex(2)

#clear login verification feedback(used when changing inputs of username or password lineEdits)
def clear_step1_feedback():
    ui.step1_feedback.clear()

#setup buttons
ui.step1_check_pushButton.clicked.connect(check_account)
ui.next_step_pushButton.clicked.connect(go_step2)
#clear feedback when changing inputs
ui.username_lineEdit.textChanged.connect(clear_step1_feedback)
ui.password_lineEdit.textChanged.connect(clear_step1_feedback)

#step 2--------------->

#enable/disable next button(depend on if the checkbox is checked or not)
def toggle_next():
    ui.next_step_pushButton_2.setDisabled(True) if ui.next_step_pushButton_2.isEnabled() else ui.next_step_pushButton_2.setDisabled(False)

#switch to the final step
def go_step3():
    ui.delete_account_steps_stackedWidget.setCurrentIndex(3)

#setup button and checkBox
ui.step2_agree_checkBox.clicked.connect(toggle_next)
ui.next_step_pushButton_2.clicked.connect(go_step3)

#step 3--------------->

#check that entered text is correct
def check_text():
    if ui.specific_text_lineEdit.text() == "Delete all":
        #clear all data from database
        db_script.clear_all_info(usn)
        #switch to the exit page
        ui.delete_account_steps_stackedWidget.setCurrentIndex(4)
    #if entered text is not correct
    else:
        ui.specific_text_lineEdit.setStyleSheet("""
        QLineEdit{
            border: 2px solid red;
            }
        """)

#reset the text lineEdit(used when changing text in text lineEdit)
def reset_text_lineEdit():
    ui.specific_text_lineEdit.setStyleSheet("""
    background-color: rgb(255,255,255);
    color: rgb(0,0,0);
    border: 0;
    """)

#setup button
ui.step3_confirm_pushButton.clicked.connect(check_text)
#reset lineEdit style when changing text
ui.specific_text_lineEdit.textChanged.connect(reset_text_lineEdit)

#end------------>

#setup exit button to close the dialog
ui.go_back_pushButton.clicked.connect(cancel)