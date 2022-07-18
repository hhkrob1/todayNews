import telegram
import json
import re
import requests
import os
from everyDevelop import get_every_dev
from everyEnglish import get_every_en

# Get Env variables
news_url = os.environ['NEWSURL']
english_url = os.environ['ENGLISHURL']
iciba_url = os.environ['ICIBAURL']
moyu_url = os.environ['MOYU']
develop_url = os.environ['DEVELOPURL']
bot_token = os.environ['BOTTOKEN']
chat_id = os.environ['CHATID']
chat_id2 = os.environ['CHATID2']
chat_id3 = os.environ['CHATID3']

#
calendarData = ""

# Request News data
session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}
session.headers = headers
trans_resp = session.get(news_url)
trans_json_str = trans_resp.content.decode()
trans_json = json.loads(trans_json_str)

# Filter Data by Regex
regex = r"<p .*?>(.*?)</p>"
rresult = re.findall(regex, trans_json["data"][0]["content"])
nresult = eresult = ""
flag = False
for matchr in rresult:
    if "【微语】" in matchr:
        nresult += matchr + "\n"
        flag = False
    if "星期" in matchr or flag == True:
        if "星期" in matchr:
            calendarData = matchr
        if re.match('^(\d*?)、(.*)', matchr) != None:
            matchr = re.match('^(\d*?)、(.*)', matchr).groups()
            matchr = "{: <4s}".format(matchr[0] + ".") + matchr[1]
        nresult += matchr + "\n"
        flag = True

# Request Daily English data
# eresult = get_every_en(english_url)
eresult = get_every_en(iciba_url)

# Request Daily Develop News data
dresult = get_every_dev(develop_url, moyu_url, calendarData)

# Creat Telegram Bot and Send Message to Channel at a fixed time
# Local Test use Proxy
# my_proxy = telegram.utils.request.Request(proxy_url='socks5://127.0.0.1:7890')
# bot = telegram.Bot(token=my_token, request=my_proxy)
bot = telegram.Bot(token=bot_token)

# Send Textmessage to chat_id
bot.send_message(chat_id=chat_id, text="<b>" +
                 nresult + "</b>", protect_content=True, parse_mode=telegram.ParseMode.HTML)

# Send Photo with Caption to chat_id2
bot.send_photo(chat_id=chat_id2, protect_content=True, photo=eresult[2],caption="<b>" + eresult[0] + "\n" + eresult[1] + "</b>", parse_mode=telegram.ParseMode.HTML)

# Send Textmessage to chat_id3
bot.send_message(chat_id=chat_id3, text=dresult, protect_content=True, disable_web_page_preview=False, parse_mode=telegram.ParseMode.HTML)


if __name__ == '__main__':
    pass
