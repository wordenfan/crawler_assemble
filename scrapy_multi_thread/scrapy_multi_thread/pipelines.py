# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyMultiThreadPipeline(object):
    # 保存到数据库中对应的class
    # 1、在settings.py文件中配置
    # 2、在自己实现的爬虫类中yield item,会自动执行

    def __init__(self):
        dbparms = dict(
            host='10.1.3.2',
            db='scrapy_test',
            user='medbankrd',
            passwd='medbankrd',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,  # 指定 curosr 类型
            use_unicode=True,
        )
        # 指定擦做数据库的模块名和数据库参数参数
        self.dbpool = adbapi.ConnectionPool("pymysql", **dbparms)

    # 使用twisted将mysql插入变成异步执行,pipeline默认调用
    def process_item(self, item, spider):  # 指定操作方法和操作的数据
        query = self.dbpool.runInteraction(self._do_insert, item)
        # 指定异常处理方法
        query.addErrback(self._handle_error, item, spider)
        return item

    def _do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

    # 错误处理方法
    def _handle_error(self, failure, item, spider):
        print('--------------database operation exception!!-----------------')
        print('-------------------------------------------------------------')
        print(failure)
