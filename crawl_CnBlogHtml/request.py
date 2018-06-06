import urllib.parse
import urllib.request

# params  CategoryId=808 CategoryType=SiteHome ItemListActionName=PostList PageIndex=3 ParentCategoryId=0 TotalPostCount=4000
def getHtml(url,values):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    headers = {'User-Agent':user_agent}

#===get=====
    data = urllib.parse.urlencode(values)
    submit_url = url+'?'+data

#===post=====
    #首先对data进行转码，转化成str类型
    # postData = urllib.parse.urlencode(values)
    # #post请求只支持byte类型，所以要进行再次编码
    # postData = postData.encode('utf-8')
    # #对url和参数进行包装
    # submit_url = urllib.request.Request(url, postData)


    response_result = urllib.request.urlopen(submit_url).read()
    html = response_result.decode('utf-8')
    return html

#获取数据
def requestCnblogs(index):
    print('请求数据')
    url = 'http://www.cnblogs.com/mvc/AggSite/PostList.aspx'
    value= {
         'CategoryId':808,
         'CategoryType' : 'SiteHome',
         'ItemListActionName' :'PostList',
         'PageIndex' : index,
         'ParentCategoryId' : 0,
        'TotalPostCount' : 4000
    }
    result = getHtml(url,value)
    return result