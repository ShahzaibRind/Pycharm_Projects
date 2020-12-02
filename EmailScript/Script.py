import pandas as pd
import smtplib

SenderAddress = "<www.Shazzybaloch786@gmail.com>"
password = "Gmail786"

e = pd.read_excel("Email.xlxs")
Emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("www.Shazzybaloch786@gmail.com", "Gmail786")
msg = "Hello this is a email form python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for Email in Emails:
    server.sendmail(SenderAddress, Email, body)
server.quit()