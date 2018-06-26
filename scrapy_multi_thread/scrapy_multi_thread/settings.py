# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_multi_thread project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_multi_thread'

SPIDER_MODULES = ['scrapy_multi_thread.spiders']
NEWSPIDER_MODULE = 'scrapy_multi_thread.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_multi_thread (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language':'zh-CN,zh;q=0.8',
  'Host':'www.lagou.com',
  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36',
  'Connection':'keep-alive'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_multi_thread.middlewares.ScrapyMultiThreadSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_multi_thread.middlewares.ScrapyMultiThreadDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_multi_thread.pipelines.ScrapyMultiThreadPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

COOKIE = {'_ga': 'GA1.2.1992886460.1528164096', 'user_trace_token': '20180605100136-60b0189a-6864-11e8-91c8-525400f775ce', 'LGUID': '20180605100136-60b01bc1-6864-11e8-91c8-525400f775ce', 'WEBTJ-ID': '20180622152859-16426656f5737d-04764d3c65099c-17356950-1024000-16426656f58529',
          'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1528164096,1529652539', 'LGSID': '20180622152859-ee08a019-75ed-11e8-ad33-525400f775ce', 'PRE_UTM': 'm_cf_cpt_baidu_pc', 'PRE_HOST': 'www.baidu.com', 'PRE_SITE': 'https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3Dlagou',
          'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc', '_gid': 'GA1.2.319925302.1529652540', 'X_HTTP_TOKEN': 'a7add2acf6a6d137ecc485657757a987', 'LG_LOGIN_USER_ID': '81f93f7448dd1fae5dd21961596148ed6930de94011ecb25',
          '_putrc': 'D43179227E56D0FF', 'JSESSIONID': 'ABAAABAAAGGABCB7517959870959C4171979399E2C8D0B6', 'login': 'true', 'unick': '%E5%86%AC%E9%98%B3', 'showExpriedIndex': '1', 'showExpriedCompanyHome': '1', 'showExpriedMyPublish': '1', 'hasDeliver': '9',
          'gate_login_token': '40562ece1228ff6afed578937c6aab1a1aed0f320fad6239', 'index_location_city': '%E5%85%A8%E5%9B%BD', 'TG-TRACK-CODE': 'index_navigation', '_gat': '1', 'SEARCH_ID': 'f5504c414f9342c18a155fe0b7b89330', 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1529653961',
          'LGRID': '20180622155241-3d4bf9c9-75f1-11e8-ad35-525400f775ce'}


#Mysql数据库的配置信息
MYSQL_HOST = '10.1.3.2'
MYSQL_DBNAME = 'scrapy_test'         #数据库名字，请修改
MYSQL_USER = 'medbankrd'             #数据库账号，请修改
MYSQL_PASSWD = 'medbankrd'         #数据库密码，请修改
MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用

#控制并发
CONCURRENT_REQUESTS_PER_DOMAIN = 1  #使爬虫同时只能对每个域名发起一个请求
DOWNLOAD_DELAY =3   #每两次请求之间存在延迟时间为3秒