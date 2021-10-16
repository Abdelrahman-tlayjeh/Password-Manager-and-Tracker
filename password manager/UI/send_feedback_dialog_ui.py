# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_feedback_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(393, 662)
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        Dialog.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(72, 145, 218);")
        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(20, 20, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.email_lineEdit.setText("")
        self.email_lineEdit.setCursorPosition(0)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(20, 70, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setCursorPosition(0)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.rate_text = QtWidgets.QLabel(Dialog)
        self.rate_text.setGeometry(QtCore.QRect(10, 140, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.rate_text.setFont(font)
        self.rate_text.setObjectName("rate_text")
        self.designe_groupBox = QtWidgets.QGroupBox(Dialog)
        self.designe_groupBox.setGeometry(QtCore.QRect(10, 190, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.designe_groupBox.setFont(font)
        self.designe_groupBox.setObjectName("designe_groupBox")
        self.d0 = QtWidgets.QRadioButton(self.designe_groupBox)
        self.d0.setGeometry(QtCore.QRect(0, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d0.setFont(font)
        self.d0.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.d0.setObjectName("d0")
        self.d4 = QtWidgets.QRadioButton(self.designe_groupBox)
        self.d4.setGeometry(QtCore.QRect(200, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d4.setFont(font)
        self.d4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.d4.setObjectName("d4")
        self.d2 = QtWidgets.QRadioButton(self.designe_groupBox)
        self.d2.setGeometry(QtCore.QRect(100, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d2.setFont(font)
        self.d2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.d2.setObjectName("d2")
        self.d1 = QtWidgets.QRadioButton(self.designe_groupBox)
        self.d1.setGeometry(QtCore.QRect(50, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d1.setFont(font)
        self.d1.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.d1.setObjectName("d1")
        self.d3 = QtWidgets.QRadioButton(self.designe_groupBox)
        self.d3.setGeometry(QtCore.QRect(150, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d3.setFont(font)
        self.d3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.d3.setObjectName("d3")
        self.d5 = QtWidgets.QRadioButton(self.designe_groupBox)
        self.d5.setGeometry(QtCore.QRect(250, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d5.setFont(font)
        self.d5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.d5.setObjectName("d5")
        self.features_groupBox = QtWidgets.QGroupBox(Dialog)
        self.features_groupBox.setGeometry(QtCore.QRect(10, 270, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.features_groupBox.setFont(font)
        self.features_groupBox.setObjectName("features_groupBox")
        self.f0 = QtWidgets.QRadioButton(self.features_groupBox)
        self.f0.setGeometry(QtCore.QRect(0, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.f0.setFont(font)
        self.f0.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.f0.setObjectName("f0")
        self.f4 = QtWidgets.QRadioButton(self.features_groupBox)
        self.f4.setGeometry(QtCore.QRect(200, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.f4.setFont(font)
        self.f4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.f4.setObjectName("f4")
        self.f2 = QtWidgets.QRadioButton(self.features_groupBox)
        self.f2.setGeometry(QtCore.QRect(100, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.f2.setFont(font)
        self.f2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.f2.setObjectName("f2")
        self.f1 = QtWidgets.QRadioButton(self.features_groupBox)
        self.f1.setGeometry(QtCore.QRect(50, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.f1.setFont(font)
        self.f1.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.f1.setObjectName("f1")
        self.f3 = QtWidgets.QRadioButton(self.features_groupBox)
        self.f3.setGeometry(QtCore.QRect(150, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.f3.setFont(font)
        self.f3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.f3.setObjectName("f3")
        self.f5 = QtWidgets.QRadioButton(self.features_groupBox)
        self.f5.setGeometry(QtCore.QRect(250, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.f5.setFont(font)
        self.f5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.f5.setObjectName("f5")
        self.performance_groupBox = QtWidgets.QGroupBox(Dialog)
        self.performance_groupBox.setGeometry(QtCore.QRect(10, 350, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.performance_groupBox.setFont(font)
        self.performance_groupBox.setObjectName("performance_groupBox")
        self.p0 = QtWidgets.QRadioButton(self.performance_groupBox)
        self.p0.setGeometry(QtCore.QRect(0, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p0.setFont(font)
        self.p0.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.p0.setObjectName("p0")
        self.p4 = QtWidgets.QRadioButton(self.performance_groupBox)
        self.p4.setGeometry(QtCore.QRect(200, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p4.setFont(font)
        self.p4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.p4.setObjectName("p4")
        self.p2 = QtWidgets.QRadioButton(self.performance_groupBox)
        self.p2.setGeometry(QtCore.QRect(100, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p2.setFont(font)
        self.p2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.p2.setObjectName("p2")
        self.p1 = QtWidgets.QRadioButton(self.performance_groupBox)
        self.p1.setGeometry(QtCore.QRect(50, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p1.setFont(font)
        self.p1.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.p1.setObjectName("p1")
        self.p3 = QtWidgets.QRadioButton(self.performance_groupBox)
        self.p3.setGeometry(QtCore.QRect(150, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p3.setFont(font)
        self.p3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.p3.setObjectName("p3")
        self.p5 = QtWidgets.QRadioButton(self.performance_groupBox)
        self.p5.setGeometry(QtCore.QRect(250, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p5.setFont(font)
        self.p5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 162, 243);")
        self.p5.setObjectName("p5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 470, 391, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.send_text = QtWidgets.QLabel(Dialog)
        self.send_text.setGeometry(QtCore.QRect(10, 430, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.send_text.setFont(font)
        self.send_text.setObjectName("send_text")
        self.send_pushButton = QtWidgets.QPushButton(Dialog)
        self.send_pushButton.setGeometry(QtCore.QRect(324, 620, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.send_pushButton.setFont(font)
        self.send_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 170, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(99, 195, 255);\n"
"}")
        self.send_pushButton.setObjectName("send_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Give your feedback..."))
        self.email_lineEdit.setPlaceholderText(_translate("Dialog", "Your E-Mail..."))
        self.password_lineEdit.setPlaceholderText(_translate("Dialog", "Password..."))
        self.rate_text.setText(_translate("Dialog", "Rate the Program:"))
        self.designe_groupBox.setTitle(_translate("Dialog", "Designe:"))
        self.d0.setText(_translate("Dialog", "0"))
        self.d4.setText(_translate("Dialog", "4"))
        self.d2.setText(_translate("Dialog", "2"))
        self.d1.setText(_translate("Dialog", "1"))
        self.d3.setText(_translate("Dialog", "3"))
        self.d5.setText(_translate("Dialog", "5"))
        self.features_groupBox.setTitle(_translate("Dialog", "Features:"))
        self.f0.setText(_translate("Dialog", "0"))
        self.f4.setText(_translate("Dialog", "4"))
        self.f2.setText(_translate("Dialog", "2"))
        self.f1.setText(_translate("Dialog", "1"))
        self.f3.setText(_translate("Dialog", "3"))
        self.f5.setText(_translate("Dialog", "5"))
        self.performance_groupBox.setTitle(_translate("Dialog", "Performance:"))
        self.p0.setText(_translate("Dialog", "0"))
        self.p4.setText(_translate("Dialog", "4"))
        self.p2.setText(_translate("Dialog", "2"))
        self.p1.setText(_translate("Dialog", "1"))
        self.p3.setText(_translate("Dialog", "3"))
        self.p5.setText(_translate("Dialog", "5"))
        self.send_text.setText(_translate("Dialog", "Feel free and send what you want..."))
        self.send_pushButton.setText(_translate("Dialog", "Send"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""