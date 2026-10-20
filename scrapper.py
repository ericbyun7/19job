import requests

r = requests.get(
    "https://search.incruit.com/list/search.asp?col=job&kw=%C6%C4%C0%CC%BD%E3"
)

print(r.status_code)
print(r.headers.get("content-type"))
print(r.encoding)
print(r.text)
