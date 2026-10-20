import csv
from pathlib import Path
from urllib.parse import quote, urljoin

import requests
from bs4 import BeautifulSoup

# 검색어에 맞는 채용 공고 목록을 돌려주는 함수
def search(keyword="파이썬", pages=5):
    encoded_keyword = quote(keyword, encoding="euc-kr")
    jobs = []
    seen_links = set()

    for page in range(pages):
        startno = page * 30
        print(f"\n{page + 1}페이지 가져오는 중")
        # 사이트가 사용하는 EUC-KR 방식으로 한글 검색어를 전달해요.
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={encoded_keyword}&startno={startno}"

        r = requests.get(url, timeout=10)
        r.raise_for_status()

        print("응답 코드:", r.status_code)

        # 가져온 HTML 분석하기
        soup = BeautifulSoup(r.text, "html.parser")

        # 채용 공고가 들어 있는 li 태그 찾기
        lis = soup.select("li.c_col")

        for li in lis:
            company = li.select_one("a.cpname")
            title = li.select_one(".cell_mid .cl_top a")
            if company is None or title is None:
                continue

            # 첫 번째 span에 근무지역이 들어 있어요.
            location = li.select_one(".cell_mid .cl_md > span")

            # 공고 하나를 딕셔너리에 담기
            job = {
                "company": company.get_text(" ", strip=True),
                "title": title.get_text("", strip=True),
                "location": location.get_text(" ", strip=True) if location else "정보 없음",
                "link": urljoin(r.url, title.get("href", "")),
            }
            if job["link"] not in seen_links:
                jobs.append(job)
                seen_links.add(job["link"])
    return jobs


# 파일을 직접 실행할 때만 출력하고 CSV를 저장해요.
if __name__ == "__main__":
    jobs = search(keyword="파이썬", pages=5)
    # 모은 정보를 보기 좋게 출력하기
    print(f"\n찾은 채용 공고: {len(jobs)}개")
    for number, job in enumerate(jobs, start=1):
        print(f"\n===== {number}번 공고 =====")
        for key, value in job.items():
            print(f"{key}: {value}")

    # 엑셀에서도 열 수 있는 CSV로 저장하기
    if jobs:
        output = Path(__file__).resolve().parent / "채용공고.csv"
        with output.open("w", encoding="utf-8-sig", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(jobs[0]))
            writer.writeheader()
            writer.writerows(jobs)
        print(f"\n저장 완료: {output}")
    else:
        print("공고를 찾지 못했어요. 검색 결과나 사이트 구조를 확인해 주세요.")
