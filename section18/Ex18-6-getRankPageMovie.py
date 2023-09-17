'''
파일명: Ex18-6-getRankPageMovie.py

정리를 한번 해보세요~ 라이브러리
numpy
pandas

'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://movie.daum.net/ranking/boxoffice/weekly'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find_all('strong', class_='tit_item')

# 데이터를 저장할 데이터프레임 생성
data = {'Rank':[], 'Movie Title': []}

for idx, movie in enumerate(movie_list):
    print(f'{idx+1}위 : {movie.text.strip()}')
    data['Rank'].append(idx+1)
    data['Movie Title'].append(movie.text.strip())

# 데이터프레임 객체 생성
df = pd.DataFrame(data)

# openpyxl 모듈 필요 - pip install openpyxl
df.to_excel('movie_ranking.xlsx', index=False)

print('데이터 엑셀파일로 저장')
