# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Bjjava2Pipeline(object):

    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='123456', db='zhilianwanted', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        self.cursor.execute(
            'insert into job_information(job_position,job_city,job_experience,job_education,job_describe,job_salary,job_keyword)VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format( item['jobname'], item['city'], item['experience'], item['education'], item['job_description'], item['salary'],"php"))
        self.connect.commit()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()








