# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import re
from scrapy.http import Request
from scrapy_multi_thread.items import ScrapyMultiThreadItem
from scrapy.conf import settings

class MySpider(scrapy.spiders.Spider):
    name = 'multiThread'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']
    cookie = settings['COOKIE']

    def parse(self, response):
        se = Selector(response)
        # 如果url能够匹配到需要爬取的url就爬取  [starts-with(@href, 'https://www.lagou.com/zhaopin/')]
        if (re.match("https://www.lagou.com/",response.url)):
            src = se.xpath("//div[@class='mainNavs']/div[1]//div[@class='category-list']/a")
            for i in range(1, 3):
                # for i in range(1,len(src)+1):
                name = se.xpath("//div[@class='mainNavs']/div[1]//div[@class='category-list']/a[%d]/text()" % i).extract()  # 获取a标签中的内容
                url = se.xpath("//div[@class='mainNavs']/div[1]//div[@class='category-list']/a[%d]/@href" % i).extract()  # 获取a标签中的href属性地址
                if name and url:
                    yield Request(url=url[0], meta={'name': name[0]}, callback=self.parse_url ,cookies=self.cookie)

    def parse_url(self, response):
        name = response.meta['name']
        cookie = response.request.headers.getlist('Cookie')
        print('-----------------------------------------------cookie')
        print(cookie)
        se = Selector(response)
        if (re.match("https://www.lagou.com/", response.url)):
            src = se.xpath("//div[@id='s_position_list' ]/ul/li")
            for i in range(1, len(src) + 1):
                url = se.xpath("//div[@id='s_position_list' ]/ul/li[%d]//a[@class='position_link']/@href" % i).extract()  # 获取个招聘信息的详细页面的url
                item = ScrapyMultiThreadItem()
                item['name'] = name
                item['url'] = url[0]
                yield item
            nextPage = se.xpath("//div[@class='pager_container']/a[last()]/@href").extract()#获取下一页的地址
            if (re.match(r"https://www.lagou.com/zhaopin/\w+/\d+/",nextPage[0])):  #判断是否为最后一页
                yield Request(url=nextPage[0], meta={'name': name}, callback=self.parse_url)
                response.request.headers.getlist('Cookie')