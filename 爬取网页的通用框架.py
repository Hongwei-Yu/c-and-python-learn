import requests
def getHMLTEXT(url):
    try:
        r=requests.get(url,timeout=30)#（url）
        r.raise_for_status()#如果状态不是200，引发HTTPError异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"#产生HTTPError异常就会返回到这个expect语句
if __name__=="__main__":
    url=""
    print(getHMLTEXT(url))
#这是爬取网页的通用代码框架

