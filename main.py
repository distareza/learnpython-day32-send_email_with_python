"""
    Learn how to send email from python
    https://docs.python.org/3/library/configparser.html

"""
import configparser
import smtplib

config = configparser.ConfigParser()
with open("email.properties") as strem:
    config.read_string("[top]\n" + strem.read())

email_account = config['top']["email_account"]
email_smtp = config['top']['email_smtp']
email_port = config['top']['email_smtp_port']
email_password = config['top']['email_password']
send_address = config['top']['send_to_address']


connection = smtplib.SMTP(host=email_smtp, port=email_port)
connection.starttls()
connection.login(email_account, email_password)
connection.sendmail(from_addr=email_account, to_addrs=send_address, msg=f"To:{send_address}\nSubject:Hello\n\nHello There")
connection.close()
