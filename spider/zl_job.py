#!/usr/bin/env python
# encoding=utf-8

'''

@author: houxiaojun

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: Chinesejunzai@163.com

@software: garner

@file: zl_job.py.py

@time: 17-8-23 下午10:58

@desc:

'''


import requests
from lxml import etree
import mongo


class ZhiLianJobSpider:

    name = 'zl_job'
    def __init__(self, city=None, keywords=None):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Cookie": "LastCity=%e5%8c%97%e4%ba%ac; LastCity%5Fid=530; JSSearchModel=0; __xsptplus30=30.6.1502272314.1502272314.1%234%7C%7C%7C%7C%7C%23%23xueaEIonEhsNl2emlJhK5rGC9LOQmOYV%23; zg_did=%7B%22did%22%3A%20%2215dcb972cf31-015711f4fb975d-6315107d-100200-15dcb972cf43c%22%7D; zg_08c5bcee6e9a4c0594a5d34b79b9622a=%7B%22sid%22%3A%201502359268602%2C%22updated%22%3A%201502359268602%2C%22info%22%3A%201502359268608%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22sou.zhaopin.com%22%7D; utype=667215829; rt=97d6929bf2134a71a9ad8c5420ef7d20; dywez=95841923.1502976080.25.10.dywecsr=mail.126.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/js6/read/readhtml.jsp; _jzqx=1.1496028809.1502976081.2.jzqsr=zhaopin%2Ecom|jzqct=/.jzqsr=mail%2E126%2Ecom|jzqct=/js6/read/readhtml%2Ejsp; _qzja=1.465078639.1498558711577.1502959955399.1503026234820.1503026234820.1503026304066.0.0.0.19.10; _jzqa=1.3766657437477915000.1496028809.1503020439.1503026232.19; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1503020439,1503026232,1503322221,1503453646; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1503453646; __utmt=1; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e9%a4%90%e8%a1%a5%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e5%8c%85%e5%90%83%7c%e5%8c%85%e4%bd%8f%7c%e6%88%bf%e8%a1%a5%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4; LastSearchHistory=%7b%22Id%22%3a%22abb43eb1-f5d3-4e98-917e-f88921881fa2%22%2c%22Name%22%3a%22python+%2b+%e5%8c%97%e4%ba%ac+%2b+%e6%9c%80%e8%bf%91%e4%b8%80%e5%91%a8%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e5%258c%2597%25e4%25ba%25ac%26kw%3dpython%26sm%3d0%26isfilter%3d1%26p%3d1%26pd%3d7%22%2c%22SaveTime%22%3a%22%5c%2fDate(1503454413530%2b0800)%5c%2f%22%7d; dywea=95841923.3718908553051214000.1495372313.1503322221.1503453646.29; dywec=95841923; dyweb=95841923.11.9.1503454410123; __utma=269921210.355485063.1495372314.1503322222.1503453646.29; __utmb=269921210.11.9.1503454410126; __utmc=269921210; __utmz=269921210.1502976080.25.10.utmcsr=mail.126.com|utmccn=(referral)|utmcmd=referral|utmcct=/js6/read/readhtml.jsp; BLACKSTRIP=yes",
            # "Host": "sou.zhaopin.com",
            # "Proxy-Connection": "keep-alive",
            "Referer": "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        }

        self.baseURL = "http://sou.zhaopin.com/jobs/searchresult.ashx"

        # 请求参数
        self.params = {
            "pd": "7",  # 发布时间
            "jl": "北京",  # 地区
            "kw": "python",  # 搜索条件
            "sm": "0",
            "p": "1",
            "sf": "0",
            "st": "99999",
            "isadv": "1"
        }
        self.params['pd'] = '7'
        self.params['jl'] = city
        self.params['kw'] = keywords
        # self.params['p'] = page


    #获取响应页面
    def getlistresponse(self):

        try:
            response = requests.get(self.baseURL, params= self.params, headers = self.headers, timeout = 2)
        except Exception, e:
            print e
            return self.getlistresponse()
        else:
            return response


    #解析当前页面中的列表链接a[href]
    def parselinklist(self, response):
        html = etree.HTML(response.content)
        link_list = html.xpath('//div[@class = "newlist_list_content"]/table/tr/td/div/a/@href')
        # print link_list
        # print len(link_list)

        return link_list


    #翻页解析提取详情页链接
    def getlinklists(self, page):

        link_lists = []
        for p in range(page):
            self.params['p'] = p
            response = self.getlistresponse()
            links = self.parselinklist(response)
            for link in links:
                link_lists.append(link)

        print link_lists
        print len(link_lists)

        return link_lists


    #获取详情页
    def getdetailsresponse(self, link_lists):
        for url in link_lists:
            response = requests.get(url, headers = self.headers)
            self.parsedetails(response)


    #解析详情页
    def parsedetails(self, response):
        html = etree.HTML(response.content)
        # print type(html)
        # 招聘岗位
        position = html.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()')[0].strip()
        # print position
        # 公司名称
        company = html.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/text()')[0].strip()
        # print company
        # 职位月薪
        salary = html.xpath("/html/body/div[6]/div[1]/ul/li[1]/strong/text()")[0].strip()[:-3].encode("utf-8")
        # print salary
        # 工作地点
        workposition = html.xpath("/html/body/div[6]/div[1]/ul/li[2]/strong/a/text()")[0].strip()
        # print workposition
        # 发布时间
        releasedata = html.xpath('//*[@id="span4freshdate"]/text()')[0].strip()
        # print releasedata
        # 工作性质
        worknature = html.xpath("/html/body/div[6]/div[1]/ul/li[4]/strong/text()")[0].strip()
        # print worknature
        # 工作经验
        workbackground = html.xpath("/html/body/div[6]/div[1]/ul/li[5]/strong/text()")[0].strip()
        # print workbackground
        # 最低学历
        education = html.xpath("/html/body/div[6]/div[1]/ul/li[6]/strong/text()")[0].strip()
        # print education
        # 招聘人数
        number = int(html.xpath("/html/body/div[6]/div[1]/ul/li[7]/strong/text()")[0].strip()[:-1].encode("utf-8"))
        # print number
        # 职位类别
        positioncategory = html.xpath("/html/body/div[6]/div[1]/ul/li[8]/strong/a/text()")[0].strip()
        # print positioncategory
        # 任职要求
        jobrequirements = html.xpath('//div[@class = "tab-inner-cont"]/p/text()')[:-4]
        # print len(jobrequirements)
        # print type(jobrequirements)
        # print "===============",jobrequirements
        # for i in jobrequirements:
        #     print i
        # 工作地址
        jobaddress = html.xpath('//div[@class = "tab-inner-cont"]/h2/text()')[0].strip()
        # print "+++++++++++++++",jobaddress

        # 公司规模
        companysize = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[1]/strong/text()')[0].strip()
        # print "*****************",companysize

        # 公司性质
        companynature = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[2]/strong/text()')[0].strip()
        # print "1111111111111111",companynature

        # 公司行业
        companyindustry = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[3]/strong/a/text()')[0].strip()
        # print "2222222222222222222", companyindustry

        # 公司主页链接
        try:
            companyhome = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[4]/strong/a/@href')[0].strip()
        except IndexError:
            companyhome = "NULL"
        # print "33333333333333",companyhome

        # 公司地址
        try:
            companyaddress = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[5]/strong/text()')[0].strip()
        except IndexError:
            companyaddress = "NULL"
        # print "44444444444444", companyaddress

        try:
            # 将数据封装为字典形式进行存储
            item = {}
            item["position"] = position if position else "NULL"
            item["company"] = company if company else "NULL"
            item["salary"] = salary if salary else "NULL"
            # item["workposition"] = workposition if workposition else "NULL"
            item["releasedata"] = releasedata if releasedata else "NULL"
            item["worknature"] = worknature if worknature else "NULL"
            item["workbackground"] = workbackground if workbackground else "NULL"
            item["education"] = education if education else "NULL"
            item["number"] = number if number else "NULL"
            item["positioncategory"] = positioncategory if positioncategory else "NULL"
            item["jobrequirements"] = jobrequirements if jobrequirements else "NULL"
            item["jobaddress"] = jobaddress if jobaddress else "NULL"
            item["companysize"] = companysize if companysize else "NULL"
            item["companynature"] = companynature if companynature else "NULL"
            item["companyindustry"] = companyindustry if companyindustry else "NULL"
            item["companyhome"] = companyhome if companyhome else "NULL"
            item["companyaddress"] = companyaddress if companyaddress else "NULL"

            print item

            with open("zhao.json", "w") as f:
                f.write(str(item))

            # 存入Mongo数据库
            db = mongo.MongodbHandeler()
            db.process_item(item)

        except Exception, e:
            print "[ERR]: 智联数据提取失败....",
            print e
            raise



if __name__ == "__main__":

    city = raw_input("请输入城市名：")

    keyword = raw_input("请输入查询职位：")

    spider = ZhiLianJobSpider(city=city,keywords=keyword)

    # response = spider.getlistresponse()
    #
    # spider.parselinklist(response)

    links = spider.getlinklists(1)

    spider.getdetailsresponse(links)

    print "爬取结束"









