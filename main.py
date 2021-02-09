import smtplib, ssl
from email.message import EmailMessage

def send_email():
    port = 465
    smtp_server = "smtp.gmail.com"

    message = EmailMessage()
    content = input("Message content: \n")
    message.set_content(content)
    message["Subject"] = input("E-mail subject: \n")
    sender_email = input('Enter your e-mail adress: \n')
    message["From"] = sender_email
    password = input("Enter your e-mail password: \n")
    message['To'] = input('Receiver e-mail: \n')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.send_message(message)
            print('E-mail sent !')
            server.quit()
        except:
            print("Could not sent e-mail.")
            server.quit()

send_email()