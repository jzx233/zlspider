# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Bjjava2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    job_description = scrapy.Field()
    #jobid=scrapy.Field()