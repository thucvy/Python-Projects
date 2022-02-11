import datetime as dt, smtplib, os, random, pandas as pd, re
import os

my_email = os.environ.get("email")
password = os.environ.get("password")


now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(row["name"], row.email): (row.month, row.day) for (index, row) in data.iterrows()}
print(birthdays_dict)

for key, value in birthdays_dict.items():
    if value == today:
        name_tosend = key[0].strip()
        email_tosend = key[1]
        template = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{template}") as template:
            letter = template.read()
            new_letter = letter.replace("[NAME]", name_tosend)
            with open(f"letter_tosend/letter_for_{name_tosend}.txt", mode="w") as new_letter_file:
                new_letter_file.write(new_letter)
            with open(f"letter_tosend/letter_for_{name_tosend}.txt", mode="r") as new_letter_file:
                letter_tosend = new_letter_file.read()
                # print(letter_tosend)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_tosend,
                msg=f"Subject: HAPPY BIRTHDAY\n\n{letter_tosend}"
            )
