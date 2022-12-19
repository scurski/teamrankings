import smtplib
from email.message import EmailMessage

import requests
from bs4 import BeautifulSoup
import datetime
import re

# Get the current date
now = datetime.datetime.now()

# Format the date as a string in the desired format
weekday = now.strftime("%a")
month = now.strftime("%b")
day = now.strftime("%d").lstrip("0")
today = weekday + month + day

# Make a request to the website
response = requests.get('https://www.teamrankings.com/ncb/schedules/season/')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
# with open("schedule.html", "w") as f:
#     f.write(str(soup)

# Find the table element
table = soup.find('table')

# All table heads
heads = table.find_all('thead')
# All table bodies
bodies = table.find_all('tbody')


# Zip 'em up
found = False
for i in range(len(heads)):
    head = heads[i]
    header_row = head.find_next('tr')
    header = header_row.find_next('th')
    date = re.sub(r"\s+", "", header.text)
    # print(date)
    if date != today:
        continue

    found = True
    body = bodies[i]

    html_table = '<table>'
    html_table += head.prettify()

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
    html = body.prettify()
    msg.set_content(html, subtype='html')

    # Set the subject and other email fields
    msg['Subject'] = 'Slim Pickems Daily Email'
    msg['From'] = from_address
    msg['To'] = to_address

    # Send the email
    server.send_message(msg)

    # Disconnect from the server
    server.quit()



