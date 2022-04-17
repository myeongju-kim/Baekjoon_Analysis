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
url = "https://www.acmicpc.net/status?top=" + str(start)
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
nid = "solution-42000000"
tr = soup.find(id=nid)
# find user information from solved.ac
usr_url = "https://solved.ac/search/users?query=" + tds[1].text.strip()
usr_html = requests.get(usr_url, headers=headers).text
usr_soup = BeautifulSoup(usr_html, 'html.parser')
