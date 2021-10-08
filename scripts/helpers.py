import re

#change searchBy to be accepted by sqlite database
def modify_searchBy(key):
    conv_dict = {
        "id": "_id",
        "Username": "username",
        "E-mail": "eMail",
        "App name": "appName",
        "Password": "password",
        "Creation date": "creationDate",
        "Category": "category"
    }
    return conv_dict[key]


def checkPasswordRate(pswd):
    pts = 0
    if pswd.strip():
        if len(pswd) >= 8:
            pts += 2
        elif len(pswd) >= 6:
            pts += 1
        elif len(pswd) <= 4:
            pts -= 1

        capit, lowr, digit, spChar = None, None, None, None
        for c in pswd:
            if str(c).isupper():
                capit = True
                continue
            if str(c).islower():
                lowr = True
                continue
            if str(c).isdigit():
                digit = True
                continue
            spChar = True
            
        #add pts depending on how many different types
        pts += {1:0, 2:1, 3:2, 4:4}[[capit, lowr, digit, spChar].count(True)]

        rate = {1: "Weak", 2: "OK", 5: "Good", 6: "Strong"}
        for r in rate.keys():
            if pts <= r:
                return rate[r]


def removeEmpty(lst):
    return [elem.strip() if elem.strip() else "-" for elem in lst]


def isEmail(email):
    email_pattern = re.compile(r"\w+@\w+\.\w+")
    return bool(list(email_pattern.finditer(email)))


def isMobileNb(nb):
    mobile_pattern = re.compile(r"[+]*(\d+)(\\*)(\d4+)")
    return bool(list(mobile_pattern.finditer(nb)))

