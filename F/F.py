import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import torch
from fastai.text.all import *

class EmailSender:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
        self.smtp.starttls()
        self.smtp.login(self.sender_email, self.sender_password)

    def send_email(self, to_email, subject, content):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(content, 'html'))

        self.smtp.sendmail(self.sender_email, to_email, msg.as_string())

    def close_connection(self):
        self.smtp.quit()

def generate_dynamic_content():
   
    return f"<p>Hello, this is a dynamic content generated using PyTorch: {torch.rand(1).item()}</p>"

if __name__ == "__main__":
    sender_email = 'your_sender_email@gmail.com'
    sender_password = 'your_sender_email_password'
    to_email = 'receiver_email@example.com'
    subject = 'Job Vacancy'

    dynamic_content = generate_dynamic_content()

    email_sender = EmailSender(sender_email, sender_password)
    email_sender.send_email(to_email, subject, dynamic_content)
    email_sender.close_connection()

    print('Done!')
