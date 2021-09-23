import smtplib
import datetime as dt
import random

SENDER = "MY EMAIL"
PASSWORD = "MY PASSWORD"
RECEIVER = "EMAIL TO"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(SENDER, PASSWORD)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=RECEIVER,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
