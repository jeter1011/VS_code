import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# environment variables should be used in the future to store thee
username = 'agudelojeter@gmail.com'
password = 'NotSure5006'

def send_mail(text = "Email body", subject = "Hello World", from_email = 'jeteragudelo@gmail.com', to_emails=None, html =None ):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ",".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText("<h1> this is working </h1>", 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()



    #login to my smtp server '64.233.184.108'
    #server = smtplib.SMTP(host='smpt.gmail.com',port=587)
    server = smtplib.SMTP('64.233.184.108')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
    
