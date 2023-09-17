'''
파일명: Ex18-1-requests.py

reqeusts 라이브러리
    HTTP 요청을 보내기 위한 간편하고 인기있는 라이브러리
    이를 사용하여 웹페이지 데이터를 가져오거나, API와
    상호 작용할 수 있다.

라이브러리 설치 방법
pip install requests

'''

import requests

url = 'https://n.news.naver.com/mnews/article/277/0005314676?sid=101'
# param = {'sid':'101'}

response = requests.get(url)
print(response.text)