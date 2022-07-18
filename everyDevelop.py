import requests
import json
from bs4 import BeautifulSoup

# Get Everyday Develop News data
def get_every_dev(news_url, moyu_url, calendarData):
    # Request
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }
    session.headers = headers
    news_resp = session.get(news_url).content.decode()
    moyu_resp2 = session.get(moyu_url).content.decode()
    moyu_json = json.loads(moyu_resp2)
    moyu_res = '<b><a href="' + moyu_json.get("data").get("moyu_url") + '">' + calendarData + "</a>\n</b>"
    # Parse
    soup = BeautifulSoup(news_resp, "html.parser")
    resl = ['<a href="{}">{}</a>'.format(news_url + i.attrs.get(
    "href"), i.text) for i in soup.select('.daily>.posts .post .title a')]
    res = ""
    for i in range(len(resl)):
        res += "<b>" + "{: <4s}".format(str(i + 1)+". ") + resl[i] + "\n" + "</b>"

    # Return data
    return moyu_res + res


if __name__ == '__main__':
    pass
