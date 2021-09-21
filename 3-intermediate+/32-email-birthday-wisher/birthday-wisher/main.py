import smtplib

sender = ""
password = ""
receiver = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(from_addr=sender, to_addrs=receiver,
                        msg="Subject:Hello\n\nThis is the body of my email.")

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="pcsmomo@gmail.com",
#                     msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()
