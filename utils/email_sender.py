import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_emails(self, emails):
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)

            for email in emails:
                msg = MIMEMultipart()
                msg['From'] = email['sender']
                msg['To'] = email['recipient']
                msg['Subject'] = email['subject']
                msg.attach(MIMEText(email['body'], 'plain'))

                server.send_message(msg)