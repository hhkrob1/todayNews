import telegram
import json
import re
import requests
import os

# Get Env variables
news_url = os.environ['NewsURL']
bot_token = os.environ['BOTTOKEN']
chat_id = os.environ['CHATID']

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
result = ""
flag = False
for match in rresult:
    if "【微语】" in match:
        result += match + "\n"
        flag = False
    if "星期" in match or flag == True:
        result += match + "\n"
        flag = True

# Creat Telegram Bot and Send Message to Channel at a fixed time
# Local Test use Proxy
# my_proxy = telegram.utils.request.Request(proxy_url='socks5://127.0.0.1:7890')
# bot = telegram.Bot(token=my_token, request=my_proxy)
bot = telegram.Bot(token=bot_token)
bot.send_message(chat_id=chat_id, text="<b>" +
                 result + "</b>", parse_mode=telegram.ParseMode.HTML)
