import smtplib
import ssl


def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "sender_email"
    password = "sender_email_pass"
    receiver_email = "reciever_email"

    emailcontext = ssl.create_default_context()

    try:
        TIE_server = smtplib.SMTP(smtp_server,port)
        TIE_server.starttls(sontext=emailcontext)
        TIE_server.login(sender_email,password)

        TIE_server.sendmail(sender_email,receiver_email,message)

    except Exception as e:
        print(e)
    finally:
        TIE_server.quit()
