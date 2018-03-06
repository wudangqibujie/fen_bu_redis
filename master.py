import requests
import re
import time
import redis
from lxml import etree

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
job_redis = redis.Redis(host = "127.0.0.1")

class Clawer():
    identity = "master"
    def __init__(self):
        for i in range(13):
            url = 'http://www.qiushibaike.com/hot/page/%d/' % (i + 1)
            job_redis.sadd("my_urls",url)
    def get_content(self):
        pass

if __name__ == '__main__':
    Clawer()


