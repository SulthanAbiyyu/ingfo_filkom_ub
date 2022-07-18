import requests


def send_message(text, API_KEY, CHANNEL):
    requests.post(
        f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHANNEL}&text={text}")
    print("ingfo sent.")
