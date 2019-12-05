from bs4 import BeautifulSoup
import requests

from datetime import date

today = date.today()
current_date = today.strftime("%b %d, %Y")
print(current_date)

url = 'https://www.cbssports.com/nfl/teams/ATL/atlanta-falcons/schedule/regular/'
response = requests.get(url)
content = BeautifulSoup(response.content, 'html.parser')
opposing_team = []
game_date = []
start_time = []
game_location = []
game_channel = []

#Finding the opposing team
for game in content.findAll('span', attrs={'class':'TeamName'}):
    opposing_team.append(game.text)
print(opposing_team)

#Finding the date of the game
for game in content.findAll('span', attrs={'class':'CellGameDate'}):
    game_date.append(game.text.strip())
print(game_date)

#Finding the start time of the game
for game in content.findAll('div', attrs={'class':'CellGame'}):
    start_time.append(game.text[1:-1])
print(start_time)

#Finding the channel the game is on
tables = content.findAll('tbody')
storedTable = tables[2].findAll('td')

for row in storedTable:
    game_channel.append(row.text.strip()) 
print(game_channel[4])

#Finding the location of the game
for row in storedTable:
    game_location.append(row.text.strip())
if game_location[4] == 'Mercedes-Benz Stadium':
    print('At home')
else:
    print('Away')