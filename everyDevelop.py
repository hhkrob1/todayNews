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
    moyu_pic_url = moyu_json.get("data").get("moyu_url")
    moyu_res = ""
    while True:
        if moyu_pic_url == None:
            break
        moyu_res = moyu_pic_url
        moyu_pic_url = session.get(
            moyu_pic_url, allow_redirects=False).headers.get("location")

    moyu_res = '<b><a href="' + moyu_res + '">' + calendarData + "</a>\n</b>"
    # Parse
    soup = BeautifulSoup(news_resp, "html.parser")
    # resl = ['<a href="{}">{}</a>'.format(news_url + i.attrs.get(
    # "href"), i.text) for i in soup.select('.daily>.posts .post .title a')]
    resl = {news_url + i.attrs.get(
    "href"):i.text for i in soup.select('.daily>.posts .post .title a')}
    res = ""
    nnum = 0

    # for i in range(len(resl)):
    #     dot_str = "." if (i + 1) >=10 else ".   "
    #     res += "<b>" + "{: <4s}".format(str(i + 1)+dot_str) + resl[i] + "\n" + "</b>"

    for i, k in resl.items():
        dot_str = "." if (nnum + 1) >=10 else ".   "
        num = "{: <4s}".format(str(nnum + 1)+dot_str)
        acontent = '<a href="{}">{}</a>'.format(i,num + k)
        res += "<b>" + acontent + "\n" + "</b>"
        nnum += 1

    # Return data
    return moyu_res + res


if __name__ == '__main__':
    res = get_every_dev("https://toutiao.io","https://api.j4u.ink/v1/store/other/proxy/remote/moyu.json","123")
    print(res)
    pass
