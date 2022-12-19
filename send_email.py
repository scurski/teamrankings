import smtplib
from email.message import EmailMessage

# Set the server and port for the Gmail SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start the server connection
server.ehlo()
server.starttls()

# Login to the Gmail SMTP server using your email and password
server.login('slimpickemsdaily@gmail.com', 'biorfqvpvzlvkgyt')

# Set the from and to addresses
from_address = 'slimpickemsdaily@gmail.com'
to_address = 'iliasoscar@gmail.com'

# Create the email message
msg = EmailMessage()

# Set the HTML content of the email
html = """
<html>
  <body>
    <p>This is an <b>HTML</b> email sent with Python.</p>
  </body>
</html>
"""
msg.set_content(html, subtype='html')

# Set the subject and other email fields
msg['Subject'] = 'Testing HTML email with Python'
msg['From'] = from_address
msg['To'] = to_address

# Send the email
server.send_message(msg)

# Disconnect from the server
server.quit()
