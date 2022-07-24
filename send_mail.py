import smtplib
from email.mime.text import MIMEText

def send_mail(customer, location, license, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login ='ac8f3e3726c068'
    password = '2646f0d711a7ed'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Location: {location}</li><li>License: {license}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email="lujaina.eldelebshany@gmail.com"
    receiver_email="lujaina.eldelebshany@gmail.com"

    msg=MIMEText(message, 'html')
    msg['Subject'] = 'Harassment Report'
    msg['From'] = sender_email 
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())