# Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
# name,email,year,month,day
# YourName,your_own@email.com,today_year,today_month,today_day

import random
from datetime import datetime

today = datetime.now()
today_tupple = (today.month, today.day)

import pandas

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tupple in birthday_dict:
    birthday_person = birthday_dict[today_tupple]
    template = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    file_path = f"letter_templates/{template}"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(birthday_person["email"])
        print(contents)


