import urllib.parse
import urllib.request
import json
import random
from Module import AppInfo, IAddress


class Toolkit:
    @staticmethod
    def get_response_from_server(url, post_data):
        post_data = urllib.parse.urlencode(post_data).encode('utf-8')
        header = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'}
        req = urllib.request.Request(url, post_data, header)
        return json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

    '''
    获取12位数字和字母的随机组合
    '''

    @staticmethod
    def get_random_value():
        rd = ''
        for i in range(10):
            rd += random.choice('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
        return rd

    @staticmethod
    def get_random_number(n):
        rd = ''
        for i in range(n):
            rd += random.choice('123456789')
        return rd

    @staticmethod
    def get_user_token(name, password):
        data = {
            'loginName': name,
            'loginPass': password,
            'appName': AppInfo.AppName,
            'appVersion': AppInfo.AppVersion
        }
        return Toolkit.get_response_from_server(IAddress.Login, data)['result']['accessToken']
