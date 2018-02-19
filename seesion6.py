
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("smtp.gmail.com", "*********")

msg = "Hello!"

server.sendmail("arifmohammed582@gmail.com", "arifmohammed582@gmail.com", msg)

server.quit()
