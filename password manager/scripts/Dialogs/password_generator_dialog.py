from PyQt5 import QtWidgets
from UI.password_generator_dialog_ui import Ui_Dialog
import random
from pyperclip import copy

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

def run():
	Dialog.show()
	ui.password_lineEdit.clear()

def generate():
	pswd = generate_password(ui.size_spinBox.value(), ui.capital_checkBox.isChecked(), ui.numbers_checkBox.isChecked(), ui.chars_checkBox.isChecked())
	ui.password_lineEdit.setText(pswd)


def generate_password(size, firstCappital, containNums, containSymb):
	all_chars_lst = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
	num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symb = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '/', '?']

	#random first character and capitalize it if firstCappital=True
	firstChar = random.choice(all_chars_lst).capitalize() if firstCappital else random.choice(all_chars_lst)
	size -= 1
	#UPDATE all_chars_lst then shuffle
	if containNums:
		all_chars_lst += num
	if containSymb:
		all_chars_lst += symb
	#shuffle the list which contain all characters used in generating password
	random.shuffle(all_chars_lst)
	#generate the password
	random_chars_lst = random.sample(all_chars_lst, size)
	random_chars = "".join(random_chars_lst)
	#save and return the generated password
	password = f"{firstChar}{random_chars}"

	return password

def copy_to_clipboard():
	copy(ui.password_lineEdit.text())

ui.generate_pushButton.clicked.connect(generate)
ui.copy_pushButton.clicked.connect(copy_to_clipboard)