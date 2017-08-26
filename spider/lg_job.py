#!/usr/bin/env python
# encoding: utf-8

'''

@author: houxiaojun

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: Chinesejunzai@163.com

@software: garner

@file: lg_job.py

@time: 17-8-23 上午9:48

@desc:

'''

import requests
import json
import jsonpath
from lxml import etree
from spider.config import *
import mongo


class LaGouJobSpider:

    name = "lg_job"
    city = lg_job_city_code


    def __init__(self, city, keywords):
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "26",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "user_trace_token=20170512105119-8a482850c5bd41a88bb3db562f76113a; LGUID=20170512105121-e1688c86-36bd-11e7-bcd1-5254005c3644; JSESSIONID=ABAAABAACDBABJBB9DF8A5BB42F474C362E1D9FC0D34818; index_location_city=%E4%B8%8A%E6%B5%B7; X_HTTP_TOKEN=284d6e2cb8b7fcd6b38c1a345f5bd3a4; TG-TRACK-CODE=search_code; SEARCH_ID=bd08aa3f6a264f4dba8e4a0e6d3c881a; _gid=GA1.2.283858805.1503710173; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1503020089,1503025497,1503365695,1503710173; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1503715084; _ga=GA1.2.1436781006.1494557482; LGRID=20170826103804-960ec266-8a07-11e7-b458-525400f775ce",
            "Host": "www.lagou.com",
            "Origin":"https: //www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_python?px=new&city=%E5%8C%97%E4%BA%AC",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "None",
            "X-Requested-With": "XMLHttpRequest",
        }

        self.params= {
            "px": "new",
            "city": "北京",
            "needAddtionalResult": "false",
        }

        self.data = {
            "first": "false",
            "pn": "1",
            "kd": "python",
        }

        self.params["city"] = city
        # self.data["pn"] = page
        self.data["kd"] = keywords

        #Ajax的url
        self.baseurl = "https://www.lagou.com/jobs/positionAjax.json"

    #获取列表页响应页面
    def getlistresponse(self):
        try:
            #post请求获取响应页面
            response = requests.post(url=self.baseurl, data=self.data, params = self.params, headers = self.headers)
            print response.content  #返回的是json格式的数据
            return response
        except Exception, e:
            print e
            print "拉勾页面请求失败！"
            raise


    #解析当前页中列表页链接a[href]
    def parselinklist(self, response):

        #将json格式的数据转化为python字符串
        res = json.loads(response.content)
        #提取详情页链接中的positionId
        positionIdlist = jsonpath.jsonpath(res, "$..positionId")
        print "1111111",positionIdlist
        #详情页url模板
        origin_url = "https://www.lagou.com/jobs/{positionId}.html"

        #组装url
        link_list = []
        for id in positionIdlist:
            url = origin_url.format(positionId = id)
            print url
            link_list.append(url)

        return link_list


    #翻页并提取当页列表页中的列表链接
    def getlinklists(self):

        link_lists = []
        #模拟翻页动作
        # while True:
        j = 1
        while j <= 2:
            response = self.getlistresponse()
            links = self.parselinklist(response)
            if len(links):
                for i in links:
                    link_lists.append(i)
                self.data["pn"] = int(self.data["pn"]) + 1
                j = j + 1
            else:
                break

        return link_lists

    #获取详情页面
    def getdetailsresponse(self, link_lists):

        i = 1
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",}

        for link in link_lists:
            print "22222", link
            response = requests.get(link, headers = headers)
            print "=====", i
            #调用解析详情页函数
            self.parsedetails(response)
            i += 1


    #解析详情页
    def parsedetails(self, response):
        html = etree.HTML(response.content)
        # print type(html)
        # 招聘岗位
        try:
            position = html.xpath('/html/body/div[2]/div/div[1]/div/span/text()')[0].strip()
            print position
        except:
            print(response.content)
            raise
        # 公司名称
        company = html.xpath('//*[@id="job_company"]/dt/a/div/h2/text()')[0].strip()
        print company
        # 职位月薪
        salary = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[1]/text()")[0].strip()
        print salary
        # 工作地点
        workposition1 = html.xpath("//*[@id='job_detail']/dd[3]/div[1]/a/text()")[:-1]
        workposition1 = ''.join(workposition1)
        workposition2 = html.xpath("//*[@id='job_detail']/dd[3]/div[1]/text()")
        workposition2 = ''.join(workposition2)
        workposition2 = workposition2.split('-')
        workposition2 = ''.join(workposition2).strip()
        workposition = workposition1 + workposition2
        print workposition
        # 发布时间
        releasedata = html.xpath('/html/body/div[2]/div/div[1]/dd/p[2]/text()')[0].strip()
        print releasedata
        # 工作性质
        worknature = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[5]/text()")[0].strip()
        print worknature
        # 工作经验
        workbackground = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[3]/text()")[0].strip()
        print workbackground
        # 最低学历
        education = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[4]/text()")[0].strip()
        print education
        # 招聘人数
        number = 1
        print number
        # 职位类别
        positioncategory = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[5]/text()")[0].strip()
        print positioncategory
        # 任职要求
        jobrequirements = html.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')
        jobrequirements_str = ''.join(jobrequirements).strip()
        # print len(jobrequirements)
        # print type(jobrequirements)
        # print "===============",jobrequirements_str
        for i in jobrequirements:
            print i
        # 工作地址
        jobaddress = workposition
        print "+++++++++++++++", jobaddress

        # 公司规模
        companysize = html.xpath('//*[@id="job_company"]/dd/ul/li[3]/text()')[1].strip()
        print "*****************", companysize

        # 公司性质  发展阶段
        companynature = html.xpath('//*[@id="job_company"]/dd/ul/li[2]/text()')[1].strip()
        print "1111111111111111", companynature

        # 公司行业
        companyindustry = html.xpath('//*[@id="job_company"]/dd/ul/li[1]/text()')[1].strip()
        print "2222222222222222222", companyindustry

        # 公司主页链接
        companyhome = html.xpath('//*[@id="job_company"]/dd/ul/li/a/@href')[0].strip()
        print "33333333333333", companyhome

        # 公司地址
        companyaddress = workposition
        print "44444444444444", companyaddress


        try:
            item = {}
            item["position"] = position if position else "NULL"
            item["company"] = company if company else "NULL"
            item["salary"] = salary if salary else "NULL"
            item["workposition"] = workposition if workposition else "NULL"
            item["releasedata"] = releasedata if releasedata else "NULL"
            item["worknature"] = worknature if worknature else "NULL"
            item["workbackground"] = workbackground if workbackground else "NULL"
            item["education"] = education if education else "NULL"
            item["number"] = 1
            item["positioncategory"] = positioncategory if positioncategory else "NULL"
            item["jobrequirements"] = jobrequirements_str if jobrequirements_str else "NULL"
            item["jobaddress"] = jobaddress if jobaddress else "NULL"
            item["companysize"] = companysize if companysize else "NULL"
            item["companynature"] = companynature if companynature else "NULL"
            item["companyindustry"] = companyindustry if companyindustry else "NULL"
            item["companyhome"] = companyhome if companyhome else "NULL"
            item["companyaddress"] = companyaddress if companyaddress else "NULL"

            print item
            with open("zhao.json", "wa") as f:
                f.write(str(item))

            # 存入Mongo数据库
            # db = mongo.MongodbHandeler()
            # db.process_item(item)


        except Exception, e:
            print "[ERR]: 拉勾数据提取失败....",
            print e


    #启动爬虫
    def run(self):

        #翻页获取链接
        links = self.getlinklists()
        #解析详情页面
        self.getdetailsresponse(links)

        print "拉勾爬取成功！"


if __name__ == "__main__":

    city = raw_input("请输入爬取城市：")

    keywords = raw_input("请输入爬取的岗位：")

    # page = raw_input("请输入爬取的页数：")

    spider = LaGouJobSpider(city, keywords)

    # response = spider.getlistresponse()
    #
    # spider.parselinklist(response)

    spider.run()








































