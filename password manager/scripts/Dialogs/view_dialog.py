from PyQt5 import QtWidgets
from UI import view_dialog_ui
from appData import db_script
from scripts import helpers, generator

Dialog = QtWidgets.QDialog()
ui = view_dialog_ui.Ui_Dialog()
ui.setupUi(Dialog)

#hide unused items
ui.view_specific_groupBox.hide()
ui.custom_groupBox.hide()
#make location lineEdit read-only
ui.location_lineEdit.setReadOnly(True)

usn = None

focusStyle = ui.go_quick_view_pushButton.styleSheet()
readyStyle = ui.go_export_pushButton.styleSheet()

def run_view_dialog(username):
    global usn
    usn = username
    Dialog.exec_()
    clear_view_dialog()

#switch to export page
def switch_export():
    ui.stackedWidget.setCurrentIndex(1)
    ui.go_quick_view_pushButton.setStyleSheet(readyStyle)
    ui.go_export_pushButton.setStyleSheet(focusStyle)

#switch to quick view page
def switch_view():
    ui.stackedWidget.setCurrentIndex(0)
    ui.go_export_pushButton.setStyleSheet(readyStyle)
    ui.go_quick_view_pushButton.setStyleSheet(focusStyle)

#view all saved info
def view_all():
    ui.view_specific_groupBox.hide()
    resp = db_script.view_all_info(usn)
    results = ""
    if resp:
        for t in resp:
            results += ",".join(map(str, t))
            results += "\n" + "-"*120 + "\n"
        results += "End Of Results..."
    ui.view_textBrowser.setText(results if results else "No Results Found!")

def start_view_specific():
    ui.view_specific_groupBox.show()

def view_specific():
    resp = db_script.view_specific_info(usn, helpers.modify_searchBy(ui.search_by_comboBox.currentText()), ui.search_lineEdit.text().strip())
    results = ""
    if resp:
        for t in resp:
            results += ",".join(map(str, t))
            results += "\n" + "-"*120 + "\n"
        results += "End Of Results..."
    ui.view_textBrowser.setText(results if results else "No Results Found!")

def extension_changed(ext):
    ui.extension_label.setText(f".{ext}")

def show_customs():
    ui.custom_groupBox.show()

def hide_customs():
    ui.custom_groupBox.hide()

save_location = None

def browse_floder():
    global save_location
    save_location = QtWidgets.QFileDialog.getExistingDirectory(caption="Choose a location...")
    ui.location_lineEdit.setText(save_location)

#return the text of all checkedBoxs as []
def get_checked():
    checkBoxs = (ui.username_checkBox, ui.email_checkBox, ui.app_name_checkBox, ui.password_checkBox, ui.creation_date_checkBox, ui.category_checkBox, ui.save_date_checkBox, ui.update_date_checkBox, ui.mobile_number_checkBox, ui.password_rate_checkBox, ui.note_checkBox)
    return [box.text() for box in checkBoxs if box.isChecked()]

def export():
    fileName = ui.fileName_lineEdit.text().strip()
    #if file name entered
    if fileName and save_location.strip():
        #Export Everything(standard)
        if not ui.custom_radioButton.isChecked():
            info_lst = db_script.view_all_info(usn)
            #export to excel
            if ui.excel_radioButton.isChecked():
                if generator.generate_excel(fileName, save_location, info_lst):
                    ui.export_feedback.setStyleSheet("color: rgb(0,255,0);")
                    ui.export_feedback.setText(f"Sucessfully generated:  {fileName}.xlsx")
                else:
                    ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
                    ui.export_feedback.setText(f"[{fileName}.xlsx] already exist in choosen location!")
            #export to csv
            if ui.csv_radioButton.isChecked():
                if generator.generate_csv(fileName, save_location, info_lst):
                    ui.export_feedback.setStyleSheet("color: rgb(0,255,0);")
                    ui.export_feedback.setText(f"Sucessfully generated:  {fileName}.csv")
                else:
                    ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
                    ui.export_feedback.setText(f"[{fileName}.csv] already exist in choosen location!")
        #Export custom
        else:
            #get checked boxs
            checked = get_checked()
            #get correspon data index
            indexes = {"Username": 1, "E-mail": 2, "App name": 3, "Password": 4, "Creation Date": 5, "Category": 6, "Save date": 7, "Update date": 8, "Mobile Nb.": 9, "Pass. rate": 10, "Note": 11}
            index_lst = [indexes[d] for d in checked]
            data = db_script.view_all_info(usn)
            newData = [[dataSet[i] for i in index_lst] for dataSet in data]
            #export to excel
            if ui.excel_radioButton.isChecked():
                if generator.generate_excel(fileName, save_location, newData, header= checked):
                    ui.export_feedback.setStyleSheet("color: rgb(0,255,0);")
                    ui.export_feedback.setText(f"Sucessfully generated:  {fileName}.xlsx")
                else:
                    ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
                    ui.export_feedback.setText(f"[{fileName}.xlsx] already exist in choosen location!")
            #export to csv
            if ui.csv_radioButton.isChecked():
                if generator.generate_csv(fileName, save_location, newData, header= checked):
                    ui.export_feedback.setStyleSheet("color: rgb(0,255,0);")
                    ui.export_feedback.setText(f"Sucessfully generated:  {fileName}.csv")
                else:
                    ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
                    ui.export_feedback.setText(f"[{fileName}.csv] already exist in choosen location!")

    else:
        ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
        ui.export_feedback.setText("Please enter a file name and choose a location...")

def clear_feedback():
    ui.export_feedback.clear()

def clear_view_dialog():
    ui.view_textBrowser.clear()
    ui.view_all_radioButton.setChecked(False)
    ui.view_specific_radioButton.setChecked(False)

    ui.go_quick_view_pushButton.click()

    ui.every_thing_radioButton.setChecked(True)
    ui.custom_groupBox.hide()
    ui.export_feedback.clear()
    ui.fileName_lineEdit.clear()
    ui.location_lineEdit.clear()
    global save_location
    save_location = None
    

#setup switch buttons quick view/export
ui.go_export_pushButton.clicked.connect(switch_export)
ui.go_quick_view_pushButton.clicked.connect(switch_view)

#setup QuickView buttons
ui.view_all_radioButton.clicked.connect(view_all)
ui.view_specific_radioButton.clicked.connect(start_view_specific)
ui.search_password_pushButton.clicked.connect(view_specific)

#export
ui.export_pushButton.clicked.connect(export)
ui.custom_radioButton.clicked.connect(show_customs)
ui.every_thing_radioButton.clicked.connect(hide_customs)
ui.browse_pushButton.clicked.connect(browse_floder)
ui.csv_radioButton.clicked.connect(lambda :extension_changed("CSV"))
ui.excel_radioButton.clicked.connect(lambda: extension_changed("xlsx"))

#clear feedback on changing file name or location
ui.fileName_lineEdit.textChanged.connect(clear_feedback)
ui.location_lineEdit.textChanged.connect(clear_feedback)