# web2.py
# 웹 서버에 요청
import urllib.request
# 크롤링
from bs4 import BeautifulSoup

f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
# 페이지 1번에서 5번
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)

    print(url)
    data = urllib.request.urlopen(url)
    soup =BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")
 
    for item in cartoons:
        title = item.find("a").text.strip()
        print(title)
        f.write(title + "\n")

f.close()
print("웹 크롤링 종료~~")