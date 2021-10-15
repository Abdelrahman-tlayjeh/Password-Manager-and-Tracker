# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False) 
        Dialog.resize(560, 258)
        Dialog.setStyleSheet("background-color: rgb(90, 90, 92);\n"
"color: rgb(239, 239, 239);")
        self.feedback_label = QtWidgets.QLabel(Dialog)
        self.feedback_label.setGeometry(QtCore.QRect(10, 10, 541, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.feedback_label.setFont(font)
        self.feedback_label.setText("")
        self.feedback_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.feedback_label.setWordWrap(True)
        self.feedback_label.setObjectName("feedback_label")
        self.ok_pushButton = QtWidgets.QPushButton(Dialog)
        self.ok_pushButton.setGeometry(QtCore.QRect(342, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ok_pushButton.setFont(font)
        self.ok_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(128, 255, 158);\n"
"}")
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.return_pushButton = QtWidgets.QPushButton(Dialog)
        self.return_pushButton.setGeometry(QtCore.QRect(450, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_pushButton.setFont(font)
        self.return_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 105, 105);\n"
"}")
        self.return_pushButton.setObjectName("return_pushButton")
        self.saved_feedback_label = QtWidgets.QLabel(Dialog)
        self.saved_feedback_label.setGeometry(QtCore.QRect(10, 220, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saved_feedback_label.setFont(font)
        self.saved_feedback_label.setStyleSheet("color: rgb(81, 245, 0);")
        self.saved_feedback_label.setText("")
        self.saved_feedback_label.setObjectName("saved_feedback_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "..."))
        self.ok_pushButton.setText(_translate("Dialog", "confirm"))
        self.return_pushButton.setText(_translate("Dialog", "cancel"))
