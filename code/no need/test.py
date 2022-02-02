# # Import smtplib for the actual sending function
# import smtplib

# # Import the email modules we'll need
# from email.mime.text import MIMEText


# msg = MIMEText("hello!")

# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'test'
# msg['From'] = 'sari.heshmati@gmail.com'
# msg['To'] = 'sarinaheshmatii@gmail.com'

# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail(sari.heshmati@gmail.com, [sarinaheshmatii@gmail.com], msg.as_string())
# s.quit()




# import smtplib

# gmail_user = 'sari.heshmati@gmail.com'
# gmail_password = 'sereneA1382'

# sent_from = gmail_user
# to = ['sarinaheshmatii@gmail.com']
# subject = 'test'
# body = 'hello!'

# email_text = """\
# From: %s
# To: %s
# Subject: %s

# %s
# """ % (sent_from, ", ".join(to), subject, body)

# try:
#     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     smtp_server.ehlo()
#     smtp_server.login(gmail_user, gmail_password)
#     smtp_server.sendmail(sent_from, to, email_text)
#     smtp_server.close()
#     print ("Email sent successfully!")
# except Exception as ex:
#     print ("Something went wrong….",ex)




import smtplib 
try: 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
    smtp.starttls() 
    smtp.login("sarinaheshmati.test@gmail.com","sarina_heshmati_82")
    message = "hello!" 
    smtp.sendmail("sarinaheshmati.test@gmail.com", "sarinaheshmatii@gmail.com",message) 
    smtp.quit() 

    print ("Email sent successfully!") 
except Exception as ex: 
    print("Something went wrong....",ex)