# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1058, 768)
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        Dialog.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(239, 239, 239);")
        self.report_text = QtWidgets.QLabel(Dialog)
        self.report_text.setGeometry(QtCore.QRect(10, 10, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.report_text.setFont(font)
        self.report_text.setObjectName("report_text")
        self.important_to_change_text = QtWidgets.QLabel(Dialog)
        self.important_to_change_text.setGeometry(QtCore.QRect(20, 90, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.important_to_change_text.setFont(font)
        self.important_to_change_text.setObjectName("important_to_change_text")
        self.important_to_change_listWidget = QtWidgets.QListWidget(Dialog)
        self.important_to_change_listWidget.setGeometry(QtCore.QRect(10, 140, 711, 201))
        self.important_to_change_listWidget.setStyleSheet("QListWidget{\n"
"    border: 2px solid red;\n"
"}")
        self.important_to_change_listWidget.setObjectName("important_to_change_listWidget")
        self.important_to_change_edit_pushButton = QtWidgets.QPushButton(Dialog)
        self.important_to_change_edit_pushButton.setGeometry(QtCore.QRect(20, 360, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.important_to_change_edit_pushButton.setFont(font)
        self.important_to_change_edit_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 71, 10);\n"
"}")
        self.important_to_change_edit_pushButton.setObjectName("important_to_change_edit_pushButton")
        self.can_change_text = QtWidgets.QLabel(Dialog)
        self.can_change_text.setGeometry(QtCore.QRect(20, 420, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.can_change_text.setFont(font)
        self.can_change_text.setObjectName("can_change_text")
        self.can_change_listWidget = QtWidgets.QListWidget(Dialog)
        self.can_change_listWidget.setGeometry(QtCore.QRect(10, 470, 711, 201))
        self.can_change_listWidget.setStyleSheet("QListWidget{\n"
"    border: 2px solid blue;\n"
"}")
        self.can_change_listWidget.setObjectName("can_change_listWidget")
        self.can_change_edit_pushButton = QtWidgets.QPushButton(Dialog)
        self.can_change_edit_pushButton.setGeometry(QtCore.QRect(20, 690, 93, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.can_change_edit_pushButton.setFont(font)
        self.can_change_edit_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 0, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(7, 102, 255);\n"
"}")
        self.can_change_edit_pushButton.setObjectName("can_change_edit_pushButton")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(733, 0, 20, 761))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.export_text = QtWidgets.QLabel(Dialog)
        self.export_text.setGeometry(QtCore.QRect(760, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.export_text.setFont(font)
        self.export_text.setObjectName("export_text")
        self.fileName_text = QtWidgets.QLabel(Dialog)
        self.fileName_text.setGeometry(QtCore.QRect(780, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.fileName_text.setFont(font)
        self.fileName_text.setObjectName("fileName_text")
        self.fileName_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.fileName_lineEdit.setGeometry(QtCore.QRect(770, 120, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fileName_lineEdit.setFont(font)
        self.fileName_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.fileName_lineEdit.setObjectName("fileName_lineEdit")
        self.extension_label = QtWidgets.QLabel(Dialog)
        self.extension_label.setGeometry(QtCore.QRect(990, 130, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.extension_label.setFont(font)
        self.extension_label.setObjectName("extension_label")
        self.location_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.location_lineEdit.setGeometry(QtCore.QRect(770, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.location_lineEdit.setFont(font)
        self.location_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.location_lineEdit.setObjectName("location_lineEdit")
        self.location_text = QtWidgets.QLabel(Dialog)
        self.location_text.setGeometry(QtCore.QRect(780, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.location_text.setFont(font)
        self.location_text.setObjectName("location_text")
        self.browse_pushButton = QtWidgets.QPushButton(Dialog)
        self.browse_pushButton.setGeometry(QtCore.QRect(990, 190, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.browse_pushButton.setFont(font)
        self.browse_pushButton.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: rgb(194, 194, 194);\n"
"    color: rgb(43, 43, 43)\n"
"}\n"
"QPushButton:hover{\n"
"    border: 1px solid black;\n"
"    text-decoration: underline;\n"
"    background-color: rgb(229, 229, 229);\n"
"}")
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.export_pushButton = QtWidgets.QPushButton(Dialog)
        self.export_pushButton.setGeometry(QtCore.QRect(770, 300, 111, 44))
        self.export_pushButton.setMinimumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.export_pushButton.setFont(font)
        self.export_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_pushButton.setToolTip("")
        self.export_pushButton.setStatusTip("")
        self.export_pushButton.setWhatsThis("")
        self.export_pushButton.setAccessibleName("")
        self.export_pushButton.setAccessibleDescription("")
        self.export_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(80, 161, 241);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(84, 173, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/export-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_pushButton.setIcon(icon)
        self.export_pushButton.setIconSize(QtCore.QSize(35, 35))
        self.export_pushButton.setObjectName("export_pushButton")
        self.export_feedback = QtWidgets.QLabel(Dialog)
        self.export_feedback.setGeometry(QtCore.QRect(760, 360, 291, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.export_feedback.setFont(font)
        self.export_feedback.setStyleSheet("color: rgb(255, 0, 0);")
        self.export_feedback.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.export_feedback.setWordWrap(True)
        self.export_feedback.setObjectName("export_feedback")
        self.can_change_feedback = QtWidgets.QLabel(Dialog)
        self.can_change_feedback.setGeometry(QtCore.QRect(120, 700, 601, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.can_change_feedback.setFont(font)
        self.can_change_feedback.setStyleSheet("color: rgb(255, 0, 0);")
        self.can_change_feedback.setText("")
        self.can_change_feedback.setObjectName("can_change_feedback")
        self.important_to_change_feedback = QtWidgets.QLabel(Dialog)
        self.important_to_change_feedback.setGeometry(QtCore.QRect(120, 370, 601, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.important_to_change_feedback.setFont(font)
        self.important_to_change_feedback.setStyleSheet("color: rgb(255, 0, 0);")
        self.important_to_change_feedback.setText("")
        self.important_to_change_feedback.setObjectName("important_to_change_feedback")
        self.note_groupBox = QtWidgets.QGroupBox(Dialog)
        self.note_groupBox.setGeometry(QtCore.QRect(760, 509, 291, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.note_groupBox.setFont(font)
        self.note_groupBox.setObjectName("note_groupBox")
        self.note_label = QtWidgets.QLabel(self.note_groupBox)
        self.note_label.setGeometry(QtCore.QRect(10, 30, 271, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.note_label.setFont(font)
        self.note_label.setText("")
        self.note_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.note_label.setObjectName("note_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Passwords Report"))
        self.report_text.setText(_translate("Dialog", "Report:"))
        self.important_to_change_text.setText(_translate("Dialog", "Highly recommend to change:"))
        self.important_to_change_edit_pushButton.setText(_translate("Dialog", "Edit Selected"))
        self.can_change_text.setText(_translate("Dialog", "Is Good to change:"))
        self.can_change_edit_pushButton.setText(_translate("Dialog", "Edit Selected"))
        self.export_text.setText(_translate("Dialog", "Export:"))
        self.fileName_text.setText(_translate("Dialog", "File Name:"))
        self.extension_label.setText(_translate("Dialog", ".xlsx"))
        self.location_text.setText(_translate("Dialog", "Location:"))
        self.browse_pushButton.setText(_translate("Dialog", "Browse"))
        self.export_pushButton.setText(_translate("Dialog", "Export"))
        self.export_feedback.setText(_translate("Dialog", ""))
        self.note_groupBox.setTitle(_translate("Dialog", "Note:"))


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())"""
