import json
import logging
import logging.handlers


def get_channel_data():
    # 从data数据中加载json数据

    with open(r'data\channel_data.json', "r", encoding="utf8") as f:
        json_str = f.read()
        json_py = json.loads(json_str)
        # print(json_py)
        datas = []
        for a in json_py:
            data = (a.get("channel"), a.get("num"), a.get("start"), a.get("appkey"))
            datas.append(data)
        # channel, num, start, appkey
        # print(datas)
        return datas


def init_logger(logname):
    # 获取日志器
    logger = logging.getLogger(logname)

    # 设置日志输出级别
    logger.setLevel(logging.DEBUG)

    # 日志输出到哪里 控制台
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)

    # 设置输出格式
    #fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    fmt = "'%(asctime)s - %(filename)s[line%(lineno)d] - %(levelname)s - %(message)s'"
    # 格式化器
    fmter = logging.Formatter(fmt=fmt)
    sh.setFormatter(fmter)
    # 输出到文件
    fh = logging.handlers.TimedRotatingFileHandler(r"./log/log.log", when="midnight", interval=1, backupCount=0,
                                                   encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmter)

    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger
