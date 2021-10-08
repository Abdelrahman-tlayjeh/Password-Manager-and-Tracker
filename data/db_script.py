import sqlite3

connection = sqlite3.connect("data\Password_manager_db.db")
cursor = connection.cursor()

#search for username from [USERS]
def search_user(usn):
    cursor.execute(f"""
    SELECT * FROM users WHERE username = '{usn}';
    """)
    return cursor.fetchone()

def change_login_password(usn, newPassword):
    cursor.execute(f"""
    UPDATE users
    SET password = '{newPassword}'
    WHERE username = '{usn}';
    """)
    connection.commit()

def change_remember_duration(usn, newDuration):
    cursor.execute(f"""
    UPDATE users
    SET saveLoginDuration = '{newDuration}'
    WHERE username = '{usn}';
    """)
    connection.commit()

def change_intelligence_search(usn, intel_search):
    cursor.execute(f"""
    UPDATE users
    SET intelligence_search = '{intel_search}'
    WHERE username = '{usn}';
    """)
    connection.commit()

def change_theme(usn, theme):
    cursor.execute(f"""
    UPDATE users
    SET preferredTheme = '{theme}'
    WHERE username = '{usn}';
    """)
    connection.commit()

def change_categories(usn, new_ctgs):
    cursor.execute(f"""
    UPDATE users
    SET categories = '{new_ctgs}'
    WHERE username = '{usn}';
    """)
    connection.commit()

def new_user(usn, pswd, email, categories, preferredTheme, saveLoginDuration, creationDate, loginHistory, intelSearch):
    #add new user to USERS table
    cursor.execute(f"""
    INSERT INTO users (username, password, email, categories, preferredTheme, saveLoginDuration, accountCreationDate, loginHistory, intelligence_search)
    VALUES ('{usn}', '{pswd}', '{email}', '{",".join(categories)}', '{preferredTheme}', '{saveLoginDuration}', '{creationDate}', '{",".join(loginHistory)}', '{intelSearch}');
    """)
    #create userPasswords table to the new user
    cursor.execute(f"""
    CREATE TABLE {usn}Passwords (
    _id          INTEGER       NOT NULL
                               PRIMARY KEY,
    username     VARCHAR (255),
    eMail        VARCHAR (255),
    appName      VARCHAR (255),
    password  VARCHAR (255),
    creationDate VARCHAR (255),
    category     VARCHAR (255),
    saveDate    VARCHAR (255),
    lastUpdateDate   VARCHAR (255),
    mobileNumber    VARCHAR (255),
    passwordRate    VARCHAR (255),
    note         VARCHAR (255) );
    """)
    connection.commit()

def record_login(usn, historyDate, newDate):
    #delete the oldest login
    if len(historyDate) > 30:
        #save all dates without the first(after the first time login)
        toKeep = historyDate[2:]
        #keep first time login
        historyDate = [historyDate[0]]
        #add the old dates without the oldest one
        historyDate.extend(toKeep)
    #add the new date
    historyDate.append(newDate)
    #apply change in database
    cursor.execute(f"""
    UPDATE users
    SET loginHistory = '{",".join(historyDate)}'
    WHERE username = '{usn}';
    """)
    connection.commit()

#save new informations to user INFO table
def save_info(PmUsername, data_lst):
    cursor.execute(f"""
    INSERT INTO {PmUsername}Passwords (username, eMail, appName, password, creationDate, category, saveDate, lastUpdateDate, mobileNumber, passwordRate, note)
    VALUES ('{data_lst[0]}', '{data_lst[1]}', '{data_lst[2]}', '{data_lst[3]}', '{data_lst[4]}', '{data_lst[5]}', '{data_lst[6]}', '{data_lst[7]}', '{data_lst[8]}', '{data_lst[9]}', '{data_lst[10]}');
    """)
    connection.commit()

#search informations from userPasswords table
def search_info(PmUsername, searchBy, searchKeyword, intelSearch):
    op = {"True": "LIKE", "False": "="}[intelSearch]
    cursor.execute(f"""
    SELECT * FROM {PmUsername}Passwords WHERE {searchBy} {op} '{searchKeyword}';
    """)
    return cursor.fetchall()

#update an info row
def update_info(PmUsername, info_id, new_info_lst):
    cursor.execute(f"""
    UPDATE {PmUsername}Passwords
    SET 
        username = '{new_info_lst[0]}',
        email = '{new_info_lst[1]}',
        appName = '{new_info_lst[2]}',
        password = '{new_info_lst[3]}',
        LastUpdateDate = '{new_info_lst[4]}',
        passwordRate = '{new_info_lst[5]}'
    WHERE
        _id = '{info_id}';
    """)
    connection.commit()

#delete an info row
def delete_info(PmUsername, id):
    cursor.execute(f"""
    DELETE FROM {PmUsername}Passwords WHERE _id = '{id}';
    """)
    connection.commit()

def view_all_info(PmUsername):
    cursor.execute(f"""
    SELECT * FROM {PmUsername}Passwords;
    """)
    return cursor.fetchall()

def view_specific_info(PmUsername, searchBy, searchKeyword):
    cursor.execute(f"""
    SELECT * FROM {PmUsername}Passwords WHERE {searchBy} = '{searchKeyword}';
    """)
    return cursor.fetchall()

def clear_all_info(PmUsername):
    cursor.execute(f"DELETE FROM {PmUsername}Passwords")
    connection.commit()

def clear_user(PmUsername):
    cursor.execute(f"""
    DELETE FROM users
    WHERE username = '{PmUsername}';
    """)
    cursor.execute(f"""
    DROP TABLE {PmUsername}Passwords;
    """)
    connection.commit()