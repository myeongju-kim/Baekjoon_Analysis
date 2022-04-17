import requests
import csv
from bs4 import BeautifulSoup
import time

filename='backjoon_trend.csv'
f=open(filename, 'w',encoding='utf-8-sig', newline='')
list_title=['난이도','분류','문제번호','제목','사용자', '정답', '메모리', '시간', '언어','코드길이','제출날짜']
writer=csv.writer(f)
writer.writerow(list_title)

user_agent = 'Your user agent information!!'
headers={'User-Agent':user_agent}
url = "https://www.acmicpc.net/status?top=420000020"
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
nid = "solution-42000000"
tr = soup.find(id=nid)
# find user information from solved.ac
usr_url = "https://solved.ac/search/users?query=" + tds[1].text.strip()
usr_html = requests.get(usr_url, headers=headers).text
usr_soup = BeautifulSoup(usr_html, 'html.parser')
# find queestion information from solved.ac
que_url = "https://solved.ac/search?query=" + tds[2].text
que_html = requests.get(que_url, headers=headers).text
que_soup = BeautifulSoup(que_html, 'html.parser')
que_title = que_soup.find(class_='__Latex__').text
que_tier = que_soup.find(class_='TierBadge__TierBadgeStyle-sc-hiokan-0 puOTB')['alt']
for algo in que_soup.find_all(class_='TagInline__TagDisplayNameContainer-sc-1tzcn2w-1 dKozlW'):
    que_al_list.append(algo.text[1:])
print(que_url, que_title, que_tier, que_al_list)