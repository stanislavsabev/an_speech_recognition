import smtplib


def sendEmail(to, content):
    server = smtplib.SMTP("smntp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("an20.olimpic@gmail.com", "balgaria20!")
    server.sendmail("an20.olimpic@gmail.com", to, content)
    server.close()
