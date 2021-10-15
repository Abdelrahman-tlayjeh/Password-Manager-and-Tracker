import smtplib
from random import randint

otp = None
def send_otp(email):
    global otp
    s = smtplib.SMTP(email, 587)
    s.starttls()
    try:
        s.login("ourGmail", "password")
        otp = randint(1000,9999)
        msg = f"Hi.\nThis is your order ;)\n {str(otp)}"
        s.sendmail("sender", email, msg)
        return(True, otp)
    except:
        return (False, )