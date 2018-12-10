import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
fromaddr = "grvkmr07121998@gmail.com"
toaddr = "grvkmr07121998@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "about Python project"
 
body = "Help me get ideas regarding projects on Python based on tkinter, RegEx, SQLite3 and basics!"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
