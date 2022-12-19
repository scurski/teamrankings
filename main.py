import requests
from bs4 import BeautifulSoup

from team import Team

# Make a request to the website
response = requests.get('https://www.teamrankings.com/ncb/trends/ats_trends/')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
# with open("schedule.html", "w") as f:
#     f.write(str(soup))

# Find the table element
table = soup.find('table')

# Find all the rows in the table
rows = table.find_all('tr')

# Iterate through the rows
teams = []
for row in rows:
    # Extract the cells in the row
    cells = row.find_all('td')
    if len(cells) == 0:
        continue

    team = Team(
        name=cells[0].text,
        ats_record=cells[1].text,
        cover_pct=cells[2].text,
        mov=cells[3].text,
        ats_margin=cells[4].text,
    )
    teams.append(team)


