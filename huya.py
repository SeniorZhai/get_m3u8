# -*- coding: UTF-8 -*-
import requests
import re
import urllib.parse
import sys

class Huya_live:
  def get_m3u8(self, url):
    try:
        room_id = urllib.parse.urlparse(url).path[1:]
        room_url = 'https://m.huya.com/' + str(room_id)
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/75.0.3770.100 Mobile Safari/537.36 '
        }
        response = requests.get(url=room_url, headers=header).text
        screenshot = re.findall(r"var picURL = '([\s\S]*?)'",response)[0]
        liveLineUrl = re.findall(r'liveLineUrl = "([\s\S]*?)";', response)[0]
        if liveLineUrl:
            return ("https:" + liveLineUrl, screenshot)
        else:
            return NULL
    except:
        return NULL


if __name__ == '__main__':
  huya = Huya_live()
  result = huya.get_m3u8(sys.argv[1])
  print(result[0])
  print(result[1])