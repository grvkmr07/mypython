import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "grvkmr07121998@gmail.com"
toaddr = "grvkmr07121998@gmail.com"


msg = MIMEMultipart() 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = " Another new feature: Email using Python "
body = "Get an attachment enclosed. I've done it using python"
msg.attach(MIMEText(body, 'plain'))
filename = "i-too-had-a-luv-story"
attachment = open("C:\\Users\\Hp\\Desktop\\i-too-had-a-luv-story.pdf", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "")#password
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
