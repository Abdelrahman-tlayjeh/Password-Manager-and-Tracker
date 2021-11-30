import json
from datetime import date

#return saved data from json file as (dict)
def return_data():
    json_file = open(r'appData\saved_login.json', 'r')
    data = json.load(json_file)
    #Process of checking is the login saved session is still valid
    #check that there is saved data
    if data["usn"]:
        #check if the login session is not unlimited(forever)
        if not data["saveLoginDuration"] == "forever":
            openDate = date(*list(map(int, data["sessionOpenDate"].split("-"))))
            duration = data["saveLoginDuration"]
            #if total numbers of days since the login is saved is more than max allowed days
            if (date.today() - openDate).days >= {"never": 0, "1day": 1, "1week": 7, "1month": 30, "1year": 365}[duration]:
                #clear data then recall this function
                clear_data()
                return return_data()

    #close the json file and resturn data
    json_file.close()
    return data

#set (None) as a value to all keys
def clear_data():
    #get data
    with open(r'appData\saved_login.json', 'r') as json_file:
        data = json.load(json_file)
    #reset all data to None
    for item in data.keys():
        data[item] = None
    #save updated data
    with open(r'appData\saved_login.json', 'w') as json_file:
        json.dump(data, json_file, indent= 4)

def update_data(usn, theme, saveLogin, catg, openDate, intel_search, isTemp):
    info = {
        'usn': usn,
        'theme': theme,
        'saveLoginDuration': saveLogin,
        'categories': catg,
        'sessionOpenDate': openDate,
        'intel_search': intel_search,
        'isTemp': isTemp
        }
    clear_data()
    with open(r'appData\saved_login.json', 'r+') as json_file:
        json.dump(info, json_file, indent= 4)
