# 编写时间 23y/02m, 编写环境 mac
# 根据BV号下载视频
# 有二维码验证，暂时只能手动获取cookie

# 获取cookie
# chrome浏览器登录 bilibili.com
# 开发者工具-网络-第一个会话-请求标头-cookie-SESSDATA字段
import requests
from bs4 import BeautifulSoup
from os import system
import re

SESSDATA='XXX'
cookies = {
    'SESSDATA': SESSDATA,
}

class download_BV:
    # BV开头的视频id
    def __init__(self, BV=None):
        self.cookies = cookies
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            }
        self.bvid = BV
        self.params = None

    def get_cid(self):
        url = 'https://www.bilibili.com/video/{}'.format(self.bvid)
        response = requests.get(url)
        print(response.status_code)
        response_BS = BeautifulSoup(response.text, 'lxml').find(string = re.compile('"cid":'))
        # print(str(response_BS))
        response_name = re.match('^.*?\"title\"\:\"(.*?)\".*$', str(response_BS))
        response_cid = re.match('^.*?\"cid\"\:(\d+).*$', str(response_BS))
        # print(response_BS)
        self.name = response_name.group(1)
        self.cid = response_cid.group(1)

    def get_params(self):
        downloadr.params = {
            'bvid': self.bvid,
            'cid': self.cid,
            'qn': '80',
            'fnval': '1',
            }
        
    def get_url(self):
        response = requests.get('https://api.bilibili.com/x/player/playurl', params=self.params, headers=self.headers, cookies=self.cookies)
        url_video = response.json().get('data').get('durl')[0].get('url')
        self.url = url_video

    def download(self):
        path = '/Users/user_name/Downloads/download_bilibili/' # 下载目录，根据自己的电脑设置
        name = path + self.name + '.mp4'
        middle = "--referer 'https://www.bilibili.com' -U 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400' -O"
        system("wget '{url}' {middle} '{name}'".format(url=self.url, middle=middle, name=name))



if __name__ == '__main__':
    # 更改BV 下载视频
    downloadr = download_BV()
    downloadr.bvid = 'BV1kS4y1T7kK'
    downloadr.get_cid()
    downloadr.get_params()
    # print(downloadr.name)
    # print(downloadr.params)
    downloadr.get_url()
    downloadr.download()
    