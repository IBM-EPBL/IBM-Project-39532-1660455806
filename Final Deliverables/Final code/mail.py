import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

class Mail():
    # mail server essentials
    smptpHost = "smtp.gmail.com"
    smtpPort = 587
    mailUName = 'jayahariprasath2001@gmail.com'
    mailPwd = 'psvpaubplcqqjtrr'
    fromMail = 'jayahariprasath2001@gmail.com'
    
    # mail body, subject
    mailSubject = ""
    mailContent = ''
    recipient = []

    def sendEmail(self, subject, content, receivers):
        msg = MIMEMultipart()

        msg['From'] = self.fromMail
        msg['To'] = ','.join(receivers)
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'html'))

        # sending the message object
        s = smtplib.SMTP(self.smptpHost, self.smtpPort)
        s.starttls()
        s.login(self.mailUName, self.mailPwd)
        msgText = msg.as_string()
        sendErrs = s.sendmail(self.fromMail, receivers, msgText)

        s.quit()
