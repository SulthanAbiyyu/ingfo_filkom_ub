import json
import os

from pengumuman.scrape import get_pengumuman
from pengumuman.telegram_bot import send_message


def ingfo():
    status = get_pengumuman()
    if status:
        print("[DEBUG] new pengumuman found.")

        data = json.loads(open('pengumuman_update.json', 'r').read())
        judul = data['judul']
        link = data['link']
        content = data['text'].strip()
        tanggal = data['tanggal']
        print("[DEBUG] new pengumuman title: ", judul[:20])

        if len(content) > 2500:
            print("[DEBUG] content is too long, cutting it..")
            content = content[:2500] + '... [selengkapnya cek sumber]'

        TEXT = f" {judul} \nTanggal: {tanggal} \n\n{content} \n\n\nSumber: {link} \n\nhttps://t.me/ingfofilkomub"
        API_KEY = os.environ['API_KEY']
        CHANNEL = os.environ['CHANNEL']

        print("[POST] sending ingfo..")
        send_message(TEXT, API_KEY, CHANNEL)
        print("[DEBUG] ingfo sent.")
    else:
        print("[DEBUG] no new pengumuman")
        pass


if __name__ == "__main__":
    ingfo()
