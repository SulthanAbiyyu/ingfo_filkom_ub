import json
import os

from pengumuman.scrape import get_pengumuman
from pengumuman.telegram_bot import send_message


def ingfo():
    status = get_pengumuman()
    if status:
        data = json.loads(open('pengumuman_update.json', 'r').read())
        judul = data['judul']
        link = data['link']
        content = data['text'].strip()
        tanggal = data['tanggal']
        print(judul)
        TEXT = f" {judul} \nTanggal: {tanggal} \n\n{content} \n\n\nSumber: {link}"
        API_KEY = os.environ['API_KEY']
        CHANNEL = os.environ['CHANNEL']
        send_message(TEXT, API_KEY, CHANNEL)
    else:
        pass


if __name__ == "__main__":
    ingfo()
