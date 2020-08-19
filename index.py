#라이블러리를 불러옴
from bs4 import BeautifulSoup
from urllib.request import urlopen

#urlopen에서 웹페이지를 불러와서 리스폰스에 넣는다
response = urlopen('https://www.zum.com/')
#뷰리플숩이라는 라이블러리를 이용해서 response를 넣어주고 html.parser로 분석한다음 그 결과를 soup에 담음
soup = BeautifulSoup(response, 'html.parser') 

i = 1
f = open("13.txt", 'w')
for anchor in soup.select("span.ah_k"):
    data = str(i) + "위 : " + anchor.get_text() + "\n"
    i = i + 1
    f.write(data)
f.close()