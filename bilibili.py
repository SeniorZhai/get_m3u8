import re

import requests


class BiliBili:

    def __init__(self, rid):
        self.rid = rid

    def get_real_url(self):
        # 先获取直播状态和真实房间号
        r_url = 'https://api.live.bilibili.com/room/v1/Room/room_init?id={}'.format(self.rid)
        with requests.Session() as s:
            res = s.get(r_url).json()
        code = res['code']
        if code == 0:
            live_status = res['data']['live_status']
            if live_status == 1:
                room_id = res['data']['room_id']

                def u(pf):
                    f_url = 'https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo'
                    params = {
                        'room_id': room_id,
                        "no_playurl" : 0,
	                    "mask" : 0,
	                    "qn" : 0,
	                    "platform" : "web",
	                    "protocol" : "0,1",
	                    "format" : "0,2",   
	                    "codec" : "0,1"
                    }
                    resp = s.get(f_url, params=params).json()
                    playurl = resp['data']['playurl_info']['playurl']['stream'][0]['format'][0]['codec'][0]
                    print(resp)
                    try:
                        real_url = playurl['url_info'][0]['host'] +  playurl['base_url']
                        return real_url
                    except KeyError or IndexError:
                        raise Exception('获取失败')

                return u('h5')
            else:
                raise Exception('未开播')
        else:
            raise Exception('房间不存在')


def get_real_url(rid):
    try:
        bilibili = BiliBili(rid)
        return bilibili.get_real_url()
    except Exception as e:
        print('Exception：', e)
        return False


if __name__ == '__main__':
    r = input('请输入bilibili直播房间号：\n')
    print(get_real_url(22247449))
