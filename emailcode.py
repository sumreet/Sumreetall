import smtplib

sender_email = "sumreet.randhawa111@gmail.com"
rec_email = "sukh00789@gmail.com"
password= input(str("please enter the password :"))
message= "this was sent using python"
server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("login success")
#from email.message import EmailMessage
#msg=EmailMessage()
#msg['Subject']='demoEmailProject'
#msg['From']='Sumreet.kaur@crochetech.com'
#msg['To']='sumreet.randhawa111@gmail.com'
#msg.set_content("Check Emails From Sumreet")

#server=smtplib.SMTP_SSL('smtp.gmail.com',465)
#server.login("Sukh00789@gmail.com","Reet789@....")
server.sendmail(sender_email, password ,message)
print("login success")




