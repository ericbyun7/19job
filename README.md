# 웹 스크래핑 실습

Requests로 웹페이지를 요청하고 응답 상태와 HTML을 확인합니다.

## 실행 방법 (Windows CMD)

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python scrapper.py
```

`200`은 요청 성공을 뜻합니다. 응답 결과는 사이트와 네트워크 상태에 따라 달라집니다.

검색어는 `scrapper.py`의 `keyword`, 페이지 수는 `pages`에서 바꿉니다.
회사명·공고 제목·근무지역·공고 링크를 수집하고 중복 링크를 제외해 `채용공고.csv`에 저장합니다.

## Flask 화면 실행

```bat
python app.py
```

브라우저에서 http://127.0.0.1:5000/hi 를 열면 `templates/hi.html` 화면이 표시됩니다.
코드를 저장하면 개발 서버가 다시 실행되며, 종료는 터미널에서 Ctrl+C입니다.
