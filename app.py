# save this as app.py
from flask import Flask, render_template, request
from requests import RequestException
from scrapper import search

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/hi")
def hi():
    return render_template("hi.html")


@app.route("/search")
def search_page():
    data = "19기 어플리케이션과정"
    keyword = request.args.get("keyword", "").strip()
    jobs = []
    error = ""
    if keyword:
        try:
            jobs = search(keyword, pages=5)
        except RequestException:
            error = "채용 정보를 가져오지 못했어요. 잠시 후 다시 검색해 주세요."
        except UnicodeEncodeError:
            error = "검색어에 지원하지 않는 문자가 있어요. 한글이나 영어로 검색해 주세요."
    return render_template("search.html", keyword=keyword, data=data, jobs=jobs, error=error)


# python app.py로 실행하면 웹서버 시작하기
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
