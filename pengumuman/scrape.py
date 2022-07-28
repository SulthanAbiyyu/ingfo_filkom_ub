from bs4 import BeautifulSoup
import requests
import os
import json


def get_pengumuman():
    url = "https://filkom.ub.ac.id/pengumuman/"
    proxies = {
        'http': '104.37.101.73:8181',
        'http': '186.97.182.5:999',
        'http': '188.133.173.21:8080',
        'http': '66.29.156.100:80',
        'http': '122.102.118.82:8080',
        'http': '43.255.113.232:8083',
    }
    try:
        response = requests.get(url, proxies=proxies).text
    except:
        response = requests.get(url).text

    soup = BeautifulSoup(response, 'html.parser')
    semua_pengumuman = soup.find_all('h5', class_='premium-blog-entry-title')
    judul_baru = semua_pengumuman[0].text.strip()

    if not os.path.exists('pengumuman_update.json'):
        link = semua_pengumuman[0].find('a')['href']
        link_content = BeautifulSoup(
            requests.get(link).text, 'html.parser')
        tanggal = link_content.find('time')['datetime']

        try:
            link_text = link_content.find_all(
                'div', class_='entry-content')[0].text.strip()
        except:
            link_text = ""

        data_pengumuman = {
            "judul": judul_baru,
            "link": link,
            "text": link_text,
            "tanggal": tanggal
        }
        with open('pengumuman_update.json', 'w') as f:
            json.dump(data_pengumuman, f)

        return True

    else:
        with open('pengumuman_update.json', 'r') as f:
            data_pengumuman = json.loads(f.read())
            judul_lama = data_pengumuman['judul']
            f.close()

        if judul_baru != judul_lama:
            link = semua_pengumuman[0].find('a')['href']
            link_content = BeautifulSoup(
                requests.get(link).text, 'html.parser')
            tanggal = link_content.find('time')['datetime']

            try:
                link_text = link_content.find_all(
                    'div', class_='entry-content')[0].text.strip()
            except:
                link_text = ""
                
            data_pengumuman = {
                "judul": judul_baru,
                "link": link,
                "text": link_text,
                "tanggal": tanggal
            }
            with open('pengumuman_update.json', 'w') as f:
                json.dump(data_pengumuman, f)
            print("ada ingfo")
            return True

        print("no ingfo")
        return False


if "__main__" == __name__:
    get_pengumuman()
