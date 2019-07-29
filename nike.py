## parser.py
import requests
from bs4 import BeautifulSoup

req = requests.get('https://race.kra.co.kr/racehorse/profileRaceScore.do?Act=02&Sub=1&meet=1&hrNo=037483')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = ''

for i in range(1, 12):
    # print('# contents > div.tableType2 > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(7)')
    my_titles = soup.select(
        '#contents > div.tableType2 > table > tbody > tr:nth-of-type('+str(i)+') > td:nth-of-type(7)'
        # '#contents > div.tableType2 > table > tbody'
        )

print(my_titles)

## my_titles는 list 객체
# for title in my_titles:
#     for title1 in title:
#
#         print(title.text)



