import requests
import re

# Get Everyday English Sentence
def get_every_en(sentence_url):
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }
    session.headers = headers
    sentence_resp = session.get(sentence_url).content.decode()

    regex1 = r"<div class='status__content emojify'><div class='e-content' lang='en'>.*?<p>(.*?)<br />(.*?)<br /><a"
    regex2 = r"<div data-component=\"MediaGallery\".*?(https.*?\.jpg)"
    sresult1 = re.findall(regex1, sentence_resp, re.MULTILINE | re.DOTALL)
    sresult2 = re.findall(regex2, sentence_resp, re.MULTILINE | re.DOTALL)
    return sresult1[0][0], sresult1[0][1], sresult2[0]

if __name__ == '__main__':
    pass
