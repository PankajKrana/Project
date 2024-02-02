import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'pankajrbrana1306@gmail.com'
email_password = 'fvla ckdv ypgg xefx'  # Enter your email password here

email_recipient = 'jocoto3209@armablog.com'  # Replace with the recipient's email address

subject = 'how are you'
body = """how it is going"""

em = EmailMessage()
em['From'] = email_sender  # sender address
em['To'] = email_recipient  # recipient address
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
        print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")
