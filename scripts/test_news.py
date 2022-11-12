from api.new_api import Newser
import requests
import pytest
from utils import get_channel_data,init_logger
import allure

@allure.feature("新闻")
class Test_news():
    # 设置类夹具请求前，初始化一次api接口
    def setup_class(self):
        self.new_api = Newser()
        self.logger = init_logger("api")

    # 设置方法夹具请求前
    def setup(self):
        self.session = requests.Session()

    # 设置方法夹具请求后
    def teardown(self):
        # if self.session not None
        # 判断有没有session，如果有就关闭没有就忽视
        if self.session:
            self.session.close()

    # 标 记使用传参化，数据驱动

    @pytest.mark.parametrize(['channel', 'num', 'start', 'appkey'], get_channel_data())
    @allure.story("频道")
    def test_01_success(self, channel, num, start, appkey):
        r = self.new_api.get_news(self.session, channel, num, start, appkey)
        # 断言
        dainfo = "channel{},num{},start{},appkey{}".format(channel, num, start, appkey)
        with allure.step("格式化日志"):
            self.logger.info(dainfo)
        with allure.step("断言状态码"):
            assert r.status_code == 200
            allure.attach("{}".format(r.status_code))
        with allure.step("断言内容10000"):
            assert r.json().get("code") == "10000"
            allure.attach(r.json().get("code"))
        with allure.step("断言弹框信息"):
            assert "查询成功" in r.json().get("msg")
            allure.attach(r.json().get("msg"))


    @allure.story("key错误")
    def test_02_key_error(self):
        with allure.step("发请求并且获取响应内容"):
            r = self.new_api.get_news_channel(self.session, self.new_api.appkey)
        with allure.step("断言状态码"):
            assert r.status_code == 200
            allure.attach("{}".format(r.status_code))
        with allure.step("断言内容10000"):
            assert r.json().get("code") == "10000"
            allure.attach(r.json().get("code"))
        with allure.step("断言弹框信息"):
            assert "查询成功" in r.json().get("msg")
            allure.attach(r.json().get("msg"))

