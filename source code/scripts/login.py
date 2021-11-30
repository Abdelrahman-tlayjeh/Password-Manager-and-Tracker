from appData import db_script, json_script
from scripts.hash import hash
from datetime import date, datetime


def login(usn, pswd, saveLogin):
    #check that usn and pswd not empty
    if not (usn and pswd):
        return (False, "Please enter your username and password.")
    result = db_script.search_user(usn)
    #check if entered usn exist in DB and entered pswd is correct
    if result and hash(pswd)==result[2]:
        if saveLogin:
            json_script.update_data(usn, result[5], result[6], result[4] , str(date.today()), result[-1], False)
        #add the last login to login history
        db_script.record_login(usn, result[8].split(","), str(datetime.now()))
        return (True, (result[1], result[4], result[5], result[6], result[-1])) #(True, (usn, ctg, theme, saveLoginDuration, intSearch))
    else:
        return(False, "Incorrect username or password...Please try again.")

def isUsernameValid(usn):
    if len(usn) < 4:
        return (False, "username must contains at least 4 characters")
    if not usn[0].isalpha():
        return (False, "username must began with alphabet only")
    for c in str(usn):
        if not (c.isalpha() or c.isdigit()):
            return(False, "username can't contains special characters or spaces.")
    return(True, )

def signup(usn, pswd, pswd2, email):
    #Default data
    categories = ["Tools", "Education", "Social"]
    preferredTheme = "dark"
    saveLoginDuration = "forever"
    creationDate = datetime.now()
    loginHistory = [f"First time login: {str(creationDate)}"]
    intel_search = "True"

    if not (usn and pswd and pswd2):
        return (False, "Please fill all required field.")
    if db_script.search_user(usn):
        return (False, "This username is already taken!")
    usnValid = isUsernameValid(usn)
    if not usnValid[0]:
        return (False, usnValid[1])
    if len(pswd) < 4:
        return (False, "Password must contain at least 4 characters.") 
    if pswd != pswd2:
        return (False, "Passwords are not identical!")
    try:
        #set email=None if it's not entered
        email = None if not email else email
        db_script.new_user(usn, hash(pswd), email, categories, preferredTheme, saveLoginDuration, creationDate, loginHistory, intel_search)
        return (True, )
    except Exception as err:
        return (False, f"Something Went Wrong!: {err}")
