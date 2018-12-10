import smtplib

fromaddr = 'grvkmr07121998@gmail.com'  
toaddrs  = 'grvkmr07121998@gmail.com'  
msg = 'Learning email with python... Hey man! what are you up to these days?'  

username = 'grvkmr07121998'  
password = ''

server = smtplib.SMTP('smtp.gmail.com', 587)  
server.ehlo()
server.starttls()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()
