from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
from urllib import error
from http import cookiejar

def saveContract():
    url = 'http://4s_bc.medbanks.cn/authenticate'
    value = {
        '_token': 'frse8Kh5pQt6FTvQvqR7YQzBssFIFleZ1bjfLpPT',
        'username': '13812345677',
        'password': 'Medbanks'
    }
    getHtml(url, value)


def getHtml(url, values):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    headers = {'User-Agent': user_agent}


    # data = parse.urlencode(values)
    # response_result = request.urlopen(url + '?' + data).read()
    # html = response_result.decode('utf-8')




    # 使用urlencode方法转换标准格式
    logingpostdata = parse.urlencode(values).encode('utf-8')
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    # 创建Request对象
    req1 = request.Request(url=url, data=logingpostdata, headers=headers)





    #
    date_url = 'http://4s_bc.medbanks.cn/research/project'
    req2 = request.Request(url=date_url, headers=headers)

    try:
        # 使用自己创建的opener的open方法
        response1 = opener.open(req1)
        response2 = opener.open(req2)
        html1 = response1.read().decode('utf-8')
        html2 = response2.read().decode('utf-8')
        print('=========html==========')
        # print(html1)
        print(html2)

    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError:%d" % e.code)
        elif hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)



if __name__ == "__main__":
    result = saveContract()
    print(result)