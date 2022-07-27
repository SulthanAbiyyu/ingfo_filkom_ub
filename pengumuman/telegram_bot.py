import requests


def send_message(text, API_KEY, CHANNEL):
    try:
        requests.post(
        f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHANNEL}&text={text}")
        print("ingfo sent.")
    except requests.exceptions.RequestException as error:
        print("Error: ", error)
