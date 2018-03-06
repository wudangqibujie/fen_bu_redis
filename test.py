import redis
import requests
re = redis.Redis(host = "127.0.0.1",port = 6379)
url = "http://pic.qiushibaike.com/system/pictures/9795/97953081/medium/app97953081.jpg"
r = requests.get(url)
image = [1,2,3,4]
re.set("im2",image)



# f = open("test.jpg","wb")
# f.write(image)
# f.close()
