"""
    Learn how to send email from python
    https://docs.python.org/3/library/configparser.html
    https://docs.python.org/3/library/smtplib.html

"""
import configparser
import random
import smtplib
import datetime as dt

config = configparser.ConfigParser()
with open("email.properties") as stream:
    config.read_string("[top]\n" + stream.read())

email_account = config['top']["email_account"]
email_smtp = config['top']['email_smtp']
email_port = config['top']['email_smtp_port']
email_password = config['top']['email_password']
send_address = config['top']['send_to_address']


def send_mail(subject, msg):
    print("preparing mail configuration")
    connection = smtplib.SMTP(host=email_smtp, port=email_port)
    connection.starttls()
    connection.login(email_account, email_password)
    print("sending mail")
    connection.sendmail(from_addr=email_account, to_addrs=send_address,
                        msg=f"To:{send_address}\nSubject:{subject}\n\n{msg}")
    connection.close()
    print("mail sent")


now = dt.datetime.now()
day_of_week = now.strftime("%A")
with open("quotes.txt") as qoute_file:
    all_quotes = qoute_file.readlines()
    quote = random.choice(all_quotes)
    print(quote)
    send_mail(subject=f"{day_of_week} Motivation", msg=quote)
