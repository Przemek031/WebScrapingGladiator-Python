import requests
from bs4 import BeautifulSoup
import time
#na serwery nie da się dołączyć: 201,52,53,54
server = [46,301,302,47,48,49,50,51,55,56,57,58,59,60,61,62,63,64,65]
filepath = "gracze.txt"
f = open(filepath, "w", encoding="utf-8")
f.write("")
f.close()
for S in server:
    url ='https://s'+str(S)+'-en.gladiatus.gameforge.com/game/index.php?mod=highscore&t=5&d=1&sh=140479ea89df0e1c17ca89c2f193243e'
    x=1
    while x <= 20:
        print(url)
        params = {'a': x} 
        response = requests.get(url, params=params)
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        if ((soup.find('table', {'class': 'section-like narrow'}))):
            ranking_table = soup.find('table', {'class': 'section-like narrow'})
            rows = ranking_table.find_all('tr')
            x=x+1       
            f = open(filepath, "a", encoding="utf-8")
            for row in rows[1:]:
                nick_column = row.find('td', {'class': 'ellipsis'})
                nick = nick_column.text.strip()
                print(nick)
                f.write(nick+'\n')
        else:
            break
f.close()

