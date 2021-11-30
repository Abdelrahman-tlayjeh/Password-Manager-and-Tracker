from datetime import date
from PyQt5 import QtWidgets
from UI import report_dialog_ui
from appData import db_script

Dialog = QtWidgets.QDialog()
ui = report_dialog_ui.Ui_Dialog()
ui.setupUi(Dialog)

usn = None

ui.important_to_change_edit_pushButton.setDisabled(True)
ui.can_change_edit_pushButton.setDisabled(True)

def run(username):
    global usn
    usn = username
    display()
    Dialog.exec_()
    clear()


def clear():
    ui.important_to_change_feedback.clear()
    ui.important_to_change_listWidget.clear()
    ui.can_change_feedback.clear()
    ui.can_change_listWidget.clear()

    ui.important_to_change_edit_pushButton.setDisabled(True)
    ui.can_change_edit_pushButton.setDisabled(True)


from collections import Counter

def get_repeated_passwords(data):
    #extract passwords from data
    all_pass = [row[4] for row in data]
    #counts the repetition of all passwords and sort from high-->low
    all_pass_counts = dict(sorted(dict(Counter(all_pass)).items(), key= lambda x: x[1], reverse= True))
    #add 3+ repeated passwords to first list and 2 repeated passwords to the second
    repeated_passwords = [[],[]]
    for k in all_pass_counts.keys():
        #if repeated 2 time: append to [good to change]
        if all_pass_counts[k] == 2:
            repeated_passwords[1].append(k)
        #if repeated 3< time: append to [important to change]
        elif all_pass_counts[k] >= 3:
            repeated_passwords[0].append(k)
        else: break

    return repeated_passwords 

def analyse_data():
    first_lst, second_lst = [], []
    #get data
    data = db_script.view_all_info(usn)
    #get repeated passwords
    repeated_passwords = get_repeated_passwords(data)
    #loop through each tuple(info set)
    for tup in data:
        accountPass = tup[4]
        #lastUpdate = lastUpdateDate or creationDate or savedDate
        lastUpdate = tup[8].split(",")[-1].split("-") if tup[8] != "Never" else tup[5].split("/")[::-1] if tup[5] != "-" else tup[7].split("-")
        lastUpdate = date(int(lastUpdate[0]), int(lastUpdate[1]), int(lastUpdate[2]))
        accountPassRate = tup[10]
        #if password is weak and not updated for 30 day --> to imp.
        #if not updated for more than 6 month
        #if used in more than 3 different accounts --> to imp.
        if accountPassRate == "Weak":
            tup = list(tup)
            tup.append("Very weak Password.")   #add the reason in the end of data tuple
            first_lst.append(tuple(tup))
           
        if (date.today() - lastUpdate).days >= 30 and accountPassRate in ["Weak", "OK"]:
            tup = list(tup)
            tup.append("Password not updated from 30+ days.")
            first_lst.append(tuple(tup))
       
        if accountPass in repeated_passwords[0]:
            tup = list(tup)
            tup.append("Password used multiple time.")
            first_lst.append(tuple(tup))
        
        #if weak --> to good
        #if not updated for 3 month --> to good
        #if used 1< accounts --> to good
        if accountPassRate == "OK":
            tup = list(tup)
            tup.append("Password not good.")
            second_lst.append(tuple(tup))

        if (date.today() - lastUpdate).days >= 30 and accountPassRate == "Good":
            tup = list(tup)
            tup.append("Password not changed for 30+ days")
            second_lst.append(tuple(tup))

        if (date.today() - lastUpdate).days >= 60 and accountPassRate == "Strong":
            tup = list(tup)
            tup.append("Strong Password but not changed for long time (60+ days)")
            second_lst.append(tuple(tup))

        if accountPass in repeated_passwords[1]:
            tup = list(tup)
            tup.append("Password used multiple time.")
            second_lst.append(tuple(tup))


    #remove duplicated tuples
    first_lst = list(set(first_lst))
    second_lst = list(set(second_lst))
    #remove from good lst the tuples that exist in important lst
    second_lst = [t for t in second_lst if not t in first_lst]



    return [first_lst, second_lst]

result = None   #[[important to change tuples], [good to change tuples]]
def display():
    global result
    #reset external file that contains id of selected data
    with open("appData\selected_id.txt", "w") as f:
        f.write("No Selection")
    #get analysed data
    result = analyse_data()
    #display in important to change
    if result[0]:
        fin_imp_lst = []
        for i in result[0]:
            head = [elem for elem in i[1:4] if elem != "-"][0]   #first exist of (usn. email, app name)
            pswd = i[4]
            fin_imp_lst.append("__".join((head, pswd)))

        fin_imp_lst = list(dict(sorted(dict(Counter(fin_imp_lst)).items(), key= lambda x: x[1])).items())
        fin_imp_lst = [c[0] for c in fin_imp_lst]   #transform (usn__pswd, x) --> usn_pswd //[x == count]

        ui.important_to_change_listWidget.addItems(fin_imp_lst)
    #display in good to change
    if result[1]:
        fin_good_lst = []
        for x in result[1]:
            head = [elem for elem in x[1:4] if elem != "-"][0]   #first exist of (usn. email, app name)
            pswd = x[4]
            fin_good_lst.append("__".join((head, pswd)))
        
        fin_good_lst = list(dict(sorted(dict(Counter(fin_good_lst)).items(), key= lambda x: x[1])).items())
        fin_good_lst = [c[0] for c in fin_good_lst]   #transform (usn__pswd, x) --> usn_pswd [x == count]

        ui.can_change_listWidget.addItems(fin_good_lst)

#save id of selected data in external file then close the dialog
def save_selcted_id(id):
    with open("appData\selected_id.txt", "w") as f:
        f.write(str(id))
    Dialog.close()

#get the id of selected data in important to change then call save_selcted_id()
def start_edit_important():
    selected_id = ui.important_to_change_listWidget.currentRow()
    data_id = result[0][selected_id][0]
    save_selcted_id(data_id)

#get the id of selected data in good to change then call save_selcted_id()
def start_edit_good():
    selected_id = ui.important_to_change_listWidget.currentRow()
    data_id = result[1][selected_id][0]
    save_selcted_id(data_id)
    

#enable edit buttons when a row is selected
ui.important_to_change_listWidget.itemPressed.connect(lambda: ui.important_to_change_edit_pushButton.setDisabled(False))
ui.can_change_listWidget.itemPressed.connect(lambda: ui.can_change_edit_pushButton.setDisabled(False))

#edit buttons
ui.important_to_change_edit_pushButton.clicked.connect(start_edit_important)
ui.can_change_edit_pushButton.clicked.connect(start_edit_good)


#Export:
from scripts import generator

ui.location_lineEdit.setReadOnly(True)

save_location = None
#open file browser dialog
def browse():
    global save_location
    save_location = QtWidgets.QFileDialog.getExistingDirectory(caption="Choose a location...")
    ui.location_lineEdit.setText(save_location)

#export to excel file 
def export():
    fileName = ui.fileName_lineEdit.text().strip()
    #check if file name and location are entered
    if fileName and save_location:
        #join all tuples from result[0] and result[1] in report list
        report = result[0]
        if result[1]:
            report.append(*result[1])
        #excel header
        header = ("Id", "Username", "E-mail", "App Name", "Password", "Creation date", "Category", "Save date", "Last update date", "Mobile number", "Password rate", "Note", "Issue")
        #try generate excel file
        if generator.generate_excel(fileName, save_location, report, header):
                #display success feedback
                ui.export_feedback.setStyleSheet("color: rgb(0,255,0);")
                ui.export_feedback.setText(f"Sucessfully generated:  {fileName}.xlsx")
        #if file exist or an error occured
        else:
            ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
            ui.export_feedback.setText(f"[{fileName}.xlsx] already exist in choosen location!")
    #if no filename or location are entered
    else:
        ui.export_feedback.setStyleSheet("color: rgb(255,0,0);")
        ui.export_feedback.setText("Please enter file name and choose location!")

#main export buttons
ui.browse_pushButton.clicked.connect(browse)
ui.export_pushButton.clicked.connect(export)

#clear feedback when changing filename or location
ui.fileName_lineEdit.textChanged.connect(clear_fdbk := lambda: ui.export_feedback.clear())
ui.location_lineEdit.textChanged.connect(clear_fdbk)