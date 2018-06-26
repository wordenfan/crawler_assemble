# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.items import ScrapyDemoItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/']

    def start_requests(self):
        urls = [
            'http://www.meijutt.com/new100.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = ScrapyDemoItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item
