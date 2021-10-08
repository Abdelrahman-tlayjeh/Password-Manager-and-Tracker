from PyQt5 import QtWidgets
from UI.categories_dialog_ui import Ui_Dialog
from data import db_script, json_script

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

usn, ctgs = None, None
modified = None

#show the dialog and display the original categories
def run(username, categories):
    ui.save_pushButton.setEnabled(False)
    
    global usn, ctgs, modified
    usn = username
    ctgs = categories.split(",")
    modified = categories.split(",")

    display(ctgs)
    Dialog.exec_()
    ui.listWidget.clear()
    return ctgs

#display the original categories
def display(ctgs):
    ui.listWidget.addItems(ctgs)

#display categories after changing
def update_display():
    ui.listWidget.clear()
    ui.listWidget.addItems(modified)
    ui.listWidget.setCurrentRow(0)
    #check if there is changes in categories then enable save button
    if sorted(ctgs) != sorted(modified):
        ui.save_pushButton.setEnabled(True)
    #disable save button if there is no change
    else:
        ui.save_pushButton.setEnabled(False)

    #disable delete button if no items remain to delete
    if not modified:
        ui.delete_pushButton.setEnabled(False)

#delete the selected row
def delete_selected():
    modified.remove(modified[ui.listWidget.currentRow()])
    update_display()

#start adding new category (show lineEdit)
def new():
    ui.new_ctg_groupBox.show() if ui.new_ctg_groupBox.isHidden() else ui.new_ctg_groupBox.hide()

#add the entered new category
def add_new():
    global modified
    new_ctg = ui.new_ctg_lineEdit.text().strip()
    #check if there is input
    if new_ctg:
        #to prevent duplication
        if not new_ctg in modified:
            modified.append(new_ctg)
            update_display()
        #close add new ctg section
        ui.new_ctg_lineEdit.clear()
        ui.new_ctg_groupBox.hide()
    #if no input
    else:
        ui.new_ctg_lineEdit.setStyleSheet("""
        QLineEdit{
            border: 1.5px solid red;
        }
        """)

#save changes in database, json and temp_data file
def save_changes():
    #save in db
    db_script.change_categories(usn, ",".join(modified))
    #save in json
    exist_data = json_script.return_data()
    #if there is data saved in json
    if exist_data["usn"]:
        exist_data["categories"] = ",".join(modified)
        json_script.update_data(*[exist_data[key] for key in exist_data.keys()])

    global ctgs
    ctgs = modified
    #close dialog
    Dialog.close()

#close Dialog
def back():
    Dialog.close()


ui.listWidget.itemPressed.connect(lambda: ui.delete_pushButton.setEnabled(True))
ui.delete_pushButton.clicked.connect(delete_selected)
ui.add_pushButton.clicked.connect(new)
ui.add_new_ctg_pushButton.clicked.connect(add_new)
ui.new_ctg_lineEdit.textChanged.connect(lambda: ui.new_ctg_lineEdit.setStyleSheet(""))
ui.save_pushButton.clicked.connect(save_changes)
ui.return_pushButton.clicked.connect(back)