from unittest import result
import requests

def send_msg(text):
    token = "1907297658:AAF6PFeOWh8Fd7oRCrjcfkOCEx6GETUFHZM"
    chat_id = "678056623"

    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

send_msg("Salom bugungi xat")