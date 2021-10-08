# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categories_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 514)
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        Dialog.setStyleSheet("")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 311, 301))
        self.listWidget.setObjectName("listWidget")
        self.add_pushButton = QtWidgets.QPushButton(Dialog)
        self.add_pushButton.setGeometry(QtCore.QRect(20, 340, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(213, 213, 213);\n"
"    color: rgb(85, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(194, 194, 194);\n"
"}")
        self.add_pushButton.setObjectName("add_pushButton")
        self.delete_pushButton = QtWidgets.QPushButton(Dialog)
        self.delete_pushButton.setEnabled(False)
        self.delete_pushButton.setGeometry(QtCore.QRect(70, 340, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(213, 213, 213);\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(194, 194, 194);\n"
"}")
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.save_pushButton = QtWidgets.QPushButton(Dialog)
        self.save_pushButton.setEnabled(False)
        self.save_pushButton.setGeometry(QtCore.QRect(240, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setObjectName("save_pushButton")
        self.return_pushButton = QtWidgets.QPushButton(Dialog)
        self.return_pushButton.setGeometry(QtCore.QRect(10, 470, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.return_pushButton.setFont(font)
        self.return_pushButton.setObjectName("return_pushButton")
        self.new_ctg_groupBox = QtWidgets.QGroupBox(Dialog)
        self.new_ctg_groupBox.setGeometry(QtCore.QRect(0, 380, 201, 80))
        self.new_ctg_groupBox.setTitle("")
        self.new_ctg_groupBox.setObjectName("new_ctg_groupBox")
        self.add_new_ctg_pushButton = QtWidgets.QPushButton(self.new_ctg_groupBox)
        self.add_new_ctg_pushButton.setGeometry(QtCore.QRect(160, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_new_ctg_pushButton.setFont(font)
        self.add_new_ctg_pushButton.setObjectName("add_new_ctg_pushButton")
        self.new_ctg_lineEdit = QtWidgets.QLineEdit(self.new_ctg_groupBox)
        self.new_ctg_lineEdit.setGeometry(QtCore.QRect(10, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_ctg_lineEdit.setFont(font)
        self.new_ctg_lineEdit.setText("")
        self.new_ctg_lineEdit.setObjectName("new_ctg_lineEdit")

        self.new_ctg_groupBox.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_pushButton.setText(_translate("Dialog", "+"))
        self.delete_pushButton.setText(_translate("Dialog", "-"))
        self.save_pushButton.setText(_translate("Dialog", "Save"))
        self.return_pushButton.setText(_translate("Dialog", "Return"))
        self.add_new_ctg_pushButton.setText(_translate("Dialog", "add"))

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