import requests
import re
from bs4 import BeautifulSoup

url = ('https://video.varzesh3.com/video/242475/')

def download(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    link = soup.findAll('a', href=re.compile('.mp4'))
    for info in link:
        links = info.get('href')
        with requests.get(links, stream=True)as r:
            with open('video-1.mp4', 'wb')as f:
                for video in r.iter_content(chunk_size=1024):
                    f.write(video)



download(url)