# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from lxml import etree
from urllib.parse import urlencode
from bjjava2.items import Bjjava2Item


class Bjspider2Spider(scrapy.Spider):
    name = 'bjspider2'
    allowed_domains = ['fe-api.zhaopin.com']
    start_urls=['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=886&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=php&kt=3&_v=0.20738768&x-zp-page-request-id=95325f35e0ab486cbd110e49c31911db-1546828150218-705333']
    #for i in range(1, 5):
        #start_urls = ['https://fe-api.zhaopin.com/c/i/sou?start=%s&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.12200835&x-zp-page-request-id=f5720564691242b992565f657f17b0fe-1546391881923-55623' % (i * 90)]



    def parse(self, response):



        datajson = json.loads(response.body)
        #print(datajson)
        data = datajson['data']
        #print(data)
        results = data['results']
        #print(results)

        for items in results:
            item = Bjjava2Item()
            item['jobname'] = items['jobName']

            item['salary'] = items['salary']

            url1=items['positionURL']
            response = requests.get(url1)
            s = etree.HTML(response.text)

            item['job_description'] = s.xpath('//div[@class="pos-ul"]//text()')

            city=items['city']

            workingExp=items['workingExp']
            eduLevel = items['eduLevel']

            item['city']=city['display']
            item['experience'] = workingExp['name']
            item['education'] = eduLevel['name']

            yield item
        #for i in range(1,2):
           # url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(i*90)+'&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&kt=3&_v=0.45660770&x-zp-page-request-id=b013b748e02842719acf0cfa382f3fd2-1546496371270-784233' % (i * 90)
             #url='https://fe-api.zhaopin.com/c/i/sou?start='+str(i*90)+'&pageSize=90&cityId=854&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=web%E5%89%8D%E7%AB%AF&kt=3&_v=0.63234601&x-zp-page-request-id=19a5627ba37c4e9b840fe002cdc935da-1546506310223-711664'
           #url = 'https://fe-api.zhaopin.com/c/i/sou?start=%s&pageSize=90&cityId=854&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=android&kt=3&_v=0.63234601&x-zp-page-request-id=19a5627ba37c4e9b840fe002cdc935da-1546506310223-711664' % (i * 90)

            #url='https://fe-api.zhaopin.com/c/i/sou?start='+str(i*90)+'&pageSize=90&cityId=785&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.20738768&x-zp-page-request-id=95325f35e0ab486cbd110e49c31911db-1546828150218-705333'
            #yield scrapy.Request(url=url, callback=self.parse)