import trainer
from bs4 import BeautifulSoup
from pprint import pprint
import requests

def cafeteria_info():
    html = requests.get('https://www.hanseo.ac.kr/food/foodView.do?m=0504&s=hs')
    #pprint(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    # pprint(soup)

    data1 = soup.findAll('td')

    data2 = []
    result = []
    for i in range(len(data1)):
        data2.append(data1[i].get_text(separator=", "))

    for j in range(len(data2)):
        if not data2[j]:
            data2[j] = '없음'

    for k in range(len(data2)):
        result.append(data2[k])
        result.append('\n')
        if (k+1) % 4 == 0:
            result.append('\n')
    output = ''.join(result)
    print(output)
    trainer.cafeteria_update(output)

def collage_info():
    SHOW_AMOUNT = 10
    html = requests.get('https://www.hanseo.ac.kr/boardCnts/list.do?boardID=298&m=040101&s=hs')
    #pprint(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    # pprint(soup)
    get_title = []
    for i in range(SHOW_AMOUNT):
        data1 = soup.select('td > a')[i]['title']
        get_title.append(data1)

    print()
    print(get_title)
    output = '\n\n'.join(get_title)
    trainer.information_update(output, state = 'collage')

def general_info():
    SHOW_AMOUNT = 10

    html = requests.get('https://www.hanseo.ac.kr/boardCnts/list.do?boardID=299&m=040102&s=hs')
    #pprint(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    # pprint(soup)
    get_title = []
    for i in range(SHOW_AMOUNT):
        data1 = soup.select('td > a')[i]['title']
        get_title.append(data1)

    print()
    print(get_title)
    output = '\n\n'.join(get_title)
    trainer.information_update(output, state = 'general')

cafeteria_info()
collage_info()
general_info()