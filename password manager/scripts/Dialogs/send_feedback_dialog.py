from PyQt5 import QtWidgets
from UI.send_feedback_dialog_ui import Ui_Dialog
from scripts import feedback_dialog
import smtplib, ssl
import sys

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)


def run():
    feedback_dialog.show_feedback("Hi, Your connection is secure. But if you will use a google account to send your feedback, please do the following:\n 1) Go to google account settings\n 2) go to security\n 3) Enable less secure apps.")
    if feedback_dialog.feedbackIsConfirmed:
        Dialog.exec_()
        clear()
    else:
        pass

def clear():
    ui.email_lineEdit.clear()
    ui.password_lineEdit.clear()
    ui.plainTextEdit.clear()


def send_feedback():
    email = ui.email_lineEdit.text().strip()
    pswd = ui.password_lineEdit.text().strip()


    designe_rate_radioButtons = [ui.d0, ui.d1, ui.d2, ui.d3, ui.d4, ui.d5]
    feature_rate_radioButtons = [ui.f0, ui.f1, ui.f2, ui.f3, ui.f4, ui.f5]
    perf_rate_radioButtons = [ui.p0, ui.p1, ui.p2, ui.p3, ui.p4, ui.p5]

    rates = [[r.text() for r in r_lst if r.isChecked()] for r_lst in [designe_rate_radioButtons, feature_rate_radioButtons, perf_rate_radioButtons]]

    #check email and password are entered
    if not (email and pswd):
        return feedback_dialog.show_feedback("Please enter your email and your password.\nNote that the connection is encrypted (secure)...")

    #check that the rates are completed
    try:
        rates = list(map(lambda r: int(r[0]), rates))
    except:
        return feedback_dialog.show_feedback("Please complete the rating!")

    #Form the message
    message = f"""Password Manager Rate From {email}
    Designe: {rates[0]}/5
    Features: {rates[1]}/5
    Performance: {rates[2]}/5
    \n
    {ui.plainTextEdit.toPlainText().strip() if ui.plainTextEdit.toPlainText().strip() else "-"}
    """

    #Sending msg
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
            server.login(email, pswd)
            server.sendmail(email, "abdelrahmantlayjeh@gmail.com", message)
        feedback_dialog.show_feedback("Got it!\nThank you for your feedback! ")
        Dialog.close()
    except Exception as e:
        feedback_dialog.show_feedback("We cannot send the feedback, this may be because one of the following:\n - Incorrect email or password.\n - Internet connection was interrupted\n - Your account provider prevent the operation for a reason.\nPlease check your details and try again...")


ui.send_pushButton.clicked.connect(send_feedback)