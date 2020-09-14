import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host_addr = 'sender's address'
receiver_addr = ['addr1','addr2','addr3']

message = MIMEMultipart()
message['from'] = host_addr
message['To'] = ",".join(receiver_addr)
message['subject'] = 'Testing mailer'

body = 'This is a sample message for mailer testing'

message.attach(MIMEText(body,'plain'))

email="sender's address"
password="sender's password"

mail=smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()
mail.starttls()
mail.login(email,password)
text=message.as_string()
mail.sendmail(host_addr,receiver_addr,text)
mail.quit()
