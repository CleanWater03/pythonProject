'''
파일명: Ex18-4-responseCode.py

서버 요청 - request
서버 응답 - response

http 응답(response) 코드
    200번대 응답 : 성공(Success)
    300번대 응답 : 리다이렉션(Redirection)
    400번대 응답 : 클라이언트 에러(Client Error)
        ex) 404 찾을 수 없는 페이지(주소 잘못 입력)
            403 권한 문제
    500번대 응답 : 서버 에러(Server Error)
        ex) 503 서버가 요청을 처리할 준비가 되지 않음

'''

import requests
url = 'https://www.naver.com'
response = requests.get(url)
print(f'응답 코드: {response.status_code}')