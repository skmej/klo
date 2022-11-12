import requests


class Newser():

    def __init__(self):
        self.news_url = "https://way.jd.com/jisuapi/get"
        self.news_channel_url = "https://way.jd.com/jisuapi/channel"
        self.appkey = "483c6774db1fb6010e0504d76df97b01"
        # self.session = requests.Session()

    def get_news_channel(self, session, appkey):
        data = {
            "appkey": appkey
        }
        r = session.get(self.news_channel_url, params=data)
        return r

    def get_news(self, session, channel, num, start, appkey):
        data = {
            "channel": channel,
            "num": num,
            "start": start,
            "appkey": appkey
        }
        r = session.post(self.news_url, data=data)
        return r
