# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(490, 437)
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(41, 180, 239)")
        self.head_text = QtWidgets.QLabel(Dialog)
        self.head_text.setGeometry(QtCore.QRect(20, 10, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.head_text.setFont(font)
        self.head_text.setObjectName("head_text")
        self.size_text = QtWidgets.QLabel(Dialog)
        self.size_text.setGeometry(QtCore.QRect(10, 100, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.size_text.setFont(font)
        self.size_text.setObjectName("size_text")
        self.size_spinBox = QtWidgets.QSpinBox(Dialog)
        self.size_spinBox.setGeometry(QtCore.QRect(30, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.size_spinBox.setFont(font)
        self.size_spinBox.setStyleSheet("color: rgb(206, 206, 206);")
        self.size_spinBox.setMinimum(4)
        self.size_spinBox.setMaximum(25)
        self.size_spinBox.setObjectName("size_spinBox")
        self.capital_checkBox = QtWidgets.QCheckBox(Dialog)
        self.capital_checkBox.setGeometry(QtCore.QRect(240, 100, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.capital_checkBox.setFont(font)
        self.capital_checkBox.setStyleSheet("color: rgb(225, 225, 225);")
        self.capital_checkBox.setObjectName("capital_checkBox")
        self.numbers_checkBox = QtWidgets.QCheckBox(Dialog)
        self.numbers_checkBox.setGeometry(QtCore.QRect(240, 170, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.numbers_checkBox.setFont(font)
        self.numbers_checkBox.setStyleSheet("color: rgb(225, 225, 225);")
        self.numbers_checkBox.setObjectName("numbers_checkBox")
        self.chars_checkBox = QtWidgets.QCheckBox(Dialog)
        self.chars_checkBox.setGeometry(QtCore.QRect(240, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chars_checkBox.setFont(font)
        self.chars_checkBox.setStyleSheet("color: rgb(225, 225, 225);")
        self.chars_checkBox.setObjectName("chars_checkBox")
        self.include_text = QtWidgets.QLabel(Dialog)
        self.include_text.setGeometry(QtCore.QRect(230, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.include_text.setFont(font)
        self.include_text.setObjectName("include_text")
        self.generate_pushButton = QtWidgets.QPushButton(Dialog)
        self.generate_pushButton.setGeometry(QtCore.QRect(150, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.generate_pushButton.setFont(font)
        self.generate_pushButton.setAutoFillBackground(False)
        self.generate_pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(239, 239, 239);\n"
"    background-color: rgb(0, 102, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(26, 164, 255);\n"
"}")
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(10, 360, 371, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("QLineEdit{\n"
"    color: rgb(32, 73, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.password_lineEdit.setText("")
        self.password_lineEdit.setReadOnly(True)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.copy_pushButton = QtWidgets.QPushButton(Dialog)
        self.copy_pushButton.setGeometry(QtCore.QRect(390, 360, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.copy_pushButton.setFont(font)
        self.copy_pushButton.setAutoFillBackground(False)
        self.copy_pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(239, 239, 239);\n"
"    background-color: rgb(0, 102, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(26, 164, 255);\n"
"}")
        self.copy_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/white-copy-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_pushButton.setIcon(icon)
        self.copy_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.copy_pushButton.setObjectName("copy_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Generator"))
        self.head_text.setText(_translate("Dialog", "Generate a New Password!"))
        self.size_text.setText(_translate("Dialog", "Select size:"))
        self.capital_checkBox.setText(_translate("Dialog", "Start with capital"))
        self.numbers_checkBox.setText(_translate("Dialog", "Numbers"))
        self.chars_checkBox.setText(_translate("Dialog", "Special characters"))
        self.include_text.setText(_translate("Dialog", "Include:"))
        self.generate_pushButton.setText(_translate("Dialog", "Generate..."))
        self.password_lineEdit.setPlaceholderText(_translate("Dialog", "Your Password..."))


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""