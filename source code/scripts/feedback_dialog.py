from PyQt5 import QtWidgets
from UI import feedback_dialog_ui

Dialog = QtWidgets.QDialog()
ui = feedback_dialog_ui.Ui_Dialog()
ui.setupUi(Dialog)

feedbackIsConfirmed = False

def show_feedback(fdbk):
    ui.feedback_label.setText(fdbk)
    Dialog.exec_()

def confirm():
    global feedbackIsConfirmed
    feedbackIsConfirmed = True
    Dialog.close()

def cancel():
    global feedbackIsConfirmed
    feedbackIsConfirmed = False
    Dialog.close()

ui.ok_pushButton.clicked.connect(confirm)
ui.return_pushButton.clicked.connect(cancel)
