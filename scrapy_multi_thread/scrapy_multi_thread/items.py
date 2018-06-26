# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMultiThreadItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()

    def get_insert_sql(self):
        sql = "insert into list(name,url) values(%s,%s)"
        params = (self["name"], self["url"])

        return sql, params