from PyQt5.QtWidgets import QDialog, QFileDialog
from UI import more_dialog_ui
from scripts import generator


Dialog = QDialog()
ui = more_dialog_ui.Ui_Dialog()
ui.setupUi(Dialog)

ui.location_lineEdit.setReadOnly(True)

info_lst = []
save_location = ""

def run():
    Dialog.exec_()

def display_result(result_lst):
    global info_lst
    info_lst = result_lst
    lineEdits = (ui.username_label, ui.email_label, ui.appName_label, ui.password_label, ui.creationDate_label, ui.category_label, ui.saveDate_label, ui.updateDate_label, ui.mobileNumber_label, ui.passwordRate_label, ui.note_textBrowser)
    for data, elem in zip(result_lst, lineEdits):
        #last update date
        if elem == ui.updateDate_label:
            data = data.split(",")
            #display last update date
            elem.setText(data[-1])
            continue
        #others data
        elem.setText(data)

def reset_dialog():
    for l in (ui.username_label, ui.email_label, ui.appName_label, ui.password_label, ui.creationDate_label, ui.category_label, ui.saveDate_label, ui.updateDate_label, ui.mobileNumber_label, ui.passwordRate_label, ui.note_textBrowser):
        l.clear()
    ui.export_feedback.clear()

def extension_changed(ext):
    ui.extension_label.setText(f".{ext}")

def clear_feedback():
    ui.export_feedback.clear()

def browse_floder():
    global save_location
    save_location = QFileDialog.getExistingDirectory(caption="Choose a location...")
    ui.location_lineEdit.setText(save_location)

def export():
    fileName = ui.fileName_lineEdit.text().strip()
    #if file name entered
    if fileName and save_location.strip():
        #export to txt
        if ui.txt_radioButton.isChecked():
            if generator.generate_txt(fileName, save_location, {"Username":info_lst[0], "E-Mail":info_lst[1], "App name": info_lst[2], "Password":info_lst[3]}):
                ui.export_feedback.setStyleSheet("color: rgb(0,255,0);")
                ui.export_feedback.setText(f"Sucessfully generated:  {fileName}.txt")
            else:
                ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
                ui.export_feedback.setText(f"[{fileName}.txt] already exist in choosen location!")
        #export to excel
        if ui.excel_radioButton.isChecked():
            if generator.generate_excel(fileName, save_location, [info_lst]):
                ui.export_feedback.setStyleSheet("color: rgb(0,255,0);")
                ui.export_feedback.setText(f"Sucessfully generated:  {fileName}.xlsx")
            else:
                ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
                ui.export_feedback.setText(f"[{fileName}.xlsx] already exist in choosen location!")
        #export to csv
        if ui.csv_radioButton.isChecked():
            if generator.generate_csv(fileName, save_location, [info_lst]):
                ui.export_feedback.setStyleSheet("color: rgb(0,255,0);")
                ui.export_feedback.setText(f"Sucessfully generated:  {fileName}.csv")
            else:
                ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
                ui.export_feedback.setText(f"[{fileName}.csv] already exist in choosen location!")
    else:
        ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
        ui.export_feedback.setText("Please enter a file name and choose a location...")

#browse button setup
ui.browse_pushButton.clicked.connect(browse_floder)
#main export button setup
ui.export_pushButton.clicked.connect(export)
#change on-display extension when changing it from radio buttons
ui.txt_radioButton.clicked.connect(lambda: extension_changed("text"))
ui.csv_radioButton.clicked.connect(lambda: extension_changed("csv"))
ui.excel_radioButton.clicked.connect(lambda: extension_changed("xlsx"))
#clear the feedback when making change on fileName or location
ui.fileName_lineEdit.textChanged.connect(clear_feedback)
ui.location_lineEdit.textChanged.connect(clear_feedback)