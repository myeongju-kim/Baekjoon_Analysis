import requests
import csv
from bs4 import BeautifulSoup
import time

filename='baekjoon_trend.csv'
f=open(filename, 'w',encoding='utf-8-sig', newline='')
list_title=['난이도','분류','문제번호','제목','사용자', '정답', '메모리', '시간', '언어','코드길이','제출날짜']
writer=csv.writer(f)
writer.writerow(list_title)

user_agent = 'your user_agent information'
headers={'User-Agent':user_agent}

start=42049500
#42049500 = 04. 16 ~ 38000000 = 02.
while start >= 38000000:
    url = "https://www.acmicpc.net/status?top=" + str(start)
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    sign=0
    for i in range(0, 20):
        nid = "solution-" + str(start)
        row_csv = []
        tr = soup.find(id=nid)
        tds=""
        try:
            tds = tr.find_all('td')
        except:
            print("삭제된 사용자 : ", start)
            start-=1
            break
        # find question information from solved.ac
        que_url = "https://solved.ac/search?query=" + tds[2].text
        print(que_url)
        que_html = requests.get(que_url, headers=headers).text
        que_soup = BeautifulSoup(que_html, 'html.parser')
        que_title = ""
        try:
            que_title = que_soup.find(class_='__Latex__').text
            cnt=0
        except:
            sign=1
            print("너무 많은 접속 요청 : ", start)
            break
        try:
            que_tier = que_soup.find(class_='TierBadge__TierBadgeStyle-sc-hiokan-0 puOTB')['alt']
            row_csv.append(que_tier)
        except:
            row_csv.append('None')
        que_al_list = []
        for algo in que_soup.find_all(class_='TagInline__TagDisplayNameContainer-sc-1tzcn2w-1 dKozlW'):
            que_al_list.append(algo.text[1:])
        row_csv.append('/'.join(que_al_list))
        row_csv.append(tds[2].text.strip())
        row_csv.append(que_title)
        # find usr information from solved.ac
        usr_url = "https://solved.ac/search/users?query=" + tds[1].text.strip()
        usr_html = requests.get(usr_url, headers=headers).text
        usr_soup = BeautifulSoup(usr_html, 'html.parser')
        try:
            usr_tier = usr_soup.find(class_='TierBadge__TierBadgeStyle-sc-hiokan-0 puOTB')['alt']
            row_csv.append(usr_tier)
        except:
            row_csv.append('UNRANK')
        for index in range(3, 8):
            row_csv.append(tds[index].text.strip())
        row_csv.append(soup.find(class_='real-time-update show-date')['title'])
        writer.writerow(row_csv)
        print(row_csv)
        time.sleep(1)
        start -= 1

    # sleep 1 minute when too many request errors occur
    if sign==1:
        time.sleep(60)

