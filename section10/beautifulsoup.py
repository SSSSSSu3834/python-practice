# pip show 라이브러리 이름: 라이브러리 정보를 알 수 있다.
# pip list: 어떤 라이브러리가 설치되었는지 알려줌
# pip install --upgrade 이름 : 라이브러리를 업데이트할 수 있다.
# pip uninstall : 삭제

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())                                                 