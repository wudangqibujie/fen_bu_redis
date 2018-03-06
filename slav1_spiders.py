import redis
from get_content import Get_content
import threading
# import time
def slave_1():
    r = redis.Redis(host = "127.0.0.1",port = 6379)
    # time.sleep(10)
    try:
        for i in range(10):
            url = r.spop("my_urls")
            a = Get_content(url)
            data_dict = a.get_duanzi()
            print("来自奴隶1",data_dict)
            for key,value in data_dict.items():
                r.set(key,value)
    except:
        print("完毕")
    return data_dict
