import requests
import re
import json

# Get Everyday English Sentence
def get_every_en(sentence_url):
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }
    session.headers = headers
    sentence_resp = session.get(sentence_url).content.decode()
    sentence_json = json.loads(sentence_resp)
    result_sentence = result_media = []

    # First interface API
    # regex1 = r"<div class='status__content emojify'><div class='e-content' lang='en'>.*?<p>(.*?)<br />(.*?)<br /><a"
    # regex2 = r"<div data-component=\"MediaGallery\".*?(https.*?\.jpg)"
    # result_sentence = re.findall(regex1, sentence_resp, re.MULTILINE | re.DOTALL)
    # result_media = re.findall(regex2, sentence_resp, re.MULTILINE | re.DOTALL)

    # Second interface API
    result_sentence = [[sentence_json["content"], sentence_json["note"]]]
    result_media = [sentence_json["picture2"],sentence_json["tts"]]

    # Return data
    return result_sentence[0][0], result_sentence[0][1], result_media[0], result_media[1]

if __name__ == '__main__':
    pass
