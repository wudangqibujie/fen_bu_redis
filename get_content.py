import requests
from lxml import etree

class Get_content():
    def __init__(self,url):
        r = requests.get(url)
        self.html = r.text
    def get_duanzi(self):
        html = etree.HTML(self.html)
        duanzi_list = html.xpath('//div[@id="content-left"]/div')
        data = dict()
        j = 0
        for i in duanzi_list:
            j += 1
            content = i.xpath('a/div[@class="content"]/span/text()')
            # print(content)
            imge = i.xpath('div[@class="thumb"]/a/img/@src')
            # print(imge)
            if content and imge:
                data[str(j)] = {"content":content,"img":imge}
            if len(content) == 0:
                data[str(j)] = {"content":"无","img":imge}
            if len(imge) == 0:
                data[str(j)] = {"content":content,"img":"无"}
        return data

if __name__ == '__main__':
    a = Get_content("https://www.qiushibaike.com/8hr/page/13/")
    data_dict = a.get_duanzi()





