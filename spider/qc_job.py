#!/usr/bin/env python
# encoding: utf-8

'''

@author: houxiaojun

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: Chinesejunzai@163.com

@software: garner

@file: qc_job.py

@time: 17-8-23 上午9:47

@desc:

'''

import requests
from lxml import etree
from spider.config import *

import mongo

import sys
reload(sys)
sys.setdefaultencoding("utf8")

class QianChengJobSpider:

    name = 'qc_job'
    city_code = qc_job_city_code



    def __init__(self, city, keywords):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "guid=15021503299671690051; adv=adsnew%3D0%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttp%253A%252F%252Fbzclk.baidu.com%252Fadrc.php%253Ft%253D06KL00c00fZEOkb0Bs4p00uiAsaYOC9u000000IML1300000LIBnZg.THLZ_Q5n1VeHksK85yF9pywd0ZnqrHDvPjwbPhmsnj01mWbvnsKd5HuanWc3wbPawRDYwRNaPbuArRmvnDw7wjn4PWnknW7K0ADqI1YhUyPGujY1njD3rH0dPjDLFMKzUvwGujYkP6K-5y9YIZ0lQzqYTh7Wui3dnyGEmB4WUvYEIZF9mvR8TA9s5v7bTv4dUHYLrjbzn1nhmyGs5y7cRWKWwAqvHjPbnvw4Pj7PNLKvyybdphcznZufn-G4mWcsrN-VwMKpi7uLuyTq5iuo5HK-nHRzPjfzuj9Bm1bdnARdrHuBm1fvnH-WuWbsuhuB0APzm1YzPjDzP6%2526tpl%253Dtpl_10085_15730_1%2526l%253D1054828295%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%252851Job%2529-%252525E6%25252589%252525BE%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252526xp%25253Did%2528%25252522m7ad13823%25252522%2529%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D25%2526ie%253Dutf-8%2526f%253D8%2526tn%253Dbaidu%2526wd%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526rqlang%253Dcn%26%7C%26adsnum%3D789233; search=jobarea%7E%60000000%7C%21ord_field%7E%601%7C%21recentSearch0%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA2%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAc%2B%2B%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1503540443%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAc%2B%2B%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1503495067%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch2%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAc%2B%2B%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1503495039%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch3%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1502964478%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch4%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA2%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1502959298%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21collapse_expansion%7E%601%7C%21; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; NSC_tfbsdi.51kpc.dpn-159=ffffffffc3a01b2645525d5f4f58455e445a4a423660",
            "Host": "search.51job.com",
            "Referer":"http: //search.51job.com/list/000000,000000,0000,00,9,99,c%252B%252B%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=1&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",

        }

        # self.baseURL = "http://search.51job.com"

        # 请求参数
        self.params = {
            "location": "010000",
            "pub_date": "2",
            "position": "python",
            "workyear": "99",
            "page" : "1"
        }
        self.params['pub_date'] = '2'
        self.params['location'] = self.city_code[city.decode("utf-8")]
        self.params['position'] = keywords


    #获取列表页响应页面
    def getlistresponse(self):

        #url模板
        origin_url = u'http://search.51job.com/list/{location},000000,0000,00,{pub_date},99,{position},2,{page}.html?lang=c&stype=1&postchannel=0000&workyear={workyear}&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        #组装url
        url = origin_url.format(location=self.params["location"],pub_date=self.params["pub_date"],page = self.params["page"],position=self.params["position"], workyear = self.params["workyear"])
        print url
        try:
            #发起请求,解析页面
            response = requests.get(url, headers = self.headers)
            return response
        except Exception, e:
            print e
            print "前程页面请求失败。。。"
            raise


    #解析当前页中的列表链接a[href]
    def parselinklist(self, response):

        html = etree.HTML(response.content)
        #从列表页面获取详情页的链接
        link_list = html.xpath('//*[@id="resultList"]/div/p/span/a/@href')

        return link_list


    #翻页并提取页面当中的列表链接
    def getlinklists(self):

        link_lists = []

        # while True:
        j = 1
        while j <=2:
            re = self.getlistresponse()
            if len(self.parselinklist(re)):
                ra = self.parselinklist(re)
                for i in ra:
                    link_lists.append(i)
                self.params["page"] = int(self.params["page"]) + 1
                j = j + 1
            else:
                break

        return link_lists


    #获取详情页
    def getdetailsresponse(self, link_lists):
        i = 1
        for link in link_lists:
            response = requests.get(link, headers = self.headers)
            #解析详情页信息
            print "****", i
            self.parsedetails(response)

            i = i + 1


    #解析详情页信息
    def parsedetails(self, response):

        html = etree.HTML(response.content)
        # 招聘岗位
        try:
            position = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/h1/text()')[0].strip()
        except:
            position = None
        # 公司名称
        try:
            company = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[1]/a/text()')[0].strip()
        except:
            company = None
        # 职位月薪
        try:
            salary = html.xpath("/html/body/div[2]/div[2]/div[2]/div/div[1]/strong/text()")[0].strip()
        except:
            salary = "面议"
        # 工作地点
        # workposition = html.xpath("//div[@class = 'bmsg inbox']/p/text()")[0].strip()
        try:
            workposition = html.xpath("/html/body/div[2]/div[2]/div[3]/div[5]/div/p/text()")[1].strip()
        except:
            workposition = None
        # 工作经验   最低学历 招聘人数 发布时间 英语 专业
        try:
            re = html.xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span/text()')
        except:
            re = None
        res = "".join(re).strip()
        print "信息：", res
        # 找工作经验
        index = res.find("经验")
        # 找本科
        index1 = res.find("科")
        #找大专
        index11 = res.find("专")
        # 找硕士或是博士
        index2 = res.find("士")
        # 找招聘人数
        index3 = res.find("聘")
        # 找发布时间
        index4 = res.find("发布")

        #工作经验
        if index != -1:
            workbackground = res[:index ]
            print "workbackground--", workbackground
        else:
            workbackground = None
            print "workbackground--", workbackground

        #专科或是本科  硕士或是博士
        if index1 != -1:
            education = res[index1 - 1:index1 + 1]
            print "education--",education
        elif index2 != -1:
            education = res[index2 - 1:index2 + 1]
            print "education++",education
        elif index11 != -1:
            education = res[index11 - 1:index11 + 1]
            print "education11", education
        else:
            education = None
            print "education==",education

        #招聘人数
        if index3 != -1:
            if res.find("若干") != -1:
                number = 1
                print "number--", number
            else:
                number = res[index3 + 1:index3 + 2]
                print "number++", number
        else:
            number = None
            print "number==", number

        #发布时间
        if index4 != -1:
            releasedata = res[index4 - 5:index4]
            print "releasedata--",releasedata
        else:
            releasedata = None
            print "releasedata++",releasedata

        # 工作性质
        worknature = None
        # 职位类别
        try:
            positioncategory = html.xpath("//div[@class = 'mt10']/p/span[@class = 'el']/text()")
        except:
            positioncategory = None
        # 任职要求
        try:
            jobrequirements = html.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div/text()')
        except:
            jobrequirements = None

        jobrequirements_str = ''.join(jobrequirements).strip()

        # 工作地址
        try:
            jobaddress = workposition
        except:
            jobaddress = None
        # print "+++++++++++++++",jobaddress

        # 公司信息
        try:
            info = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[2]/text()')[0].strip()

            info_list = info.split('|')

            # 公司性质
            companynature = info_list[0].strip()

            # 公司规模
            companysize = info_list[1].strip()
        except:
            companynature = None
            companysize = None

        # 公司行业
        try:
            companyindustry = info_list[2].strip()
        except:
            companyindustry = None

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
            item["number"] = number if number else "NULL"
            item["positioncategory"] = positioncategory if positioncategory else "NULL"
            item["jobrequirements"] = jobrequirements_str if jobrequirements_str else "NULL"
            item["jobaddress"] = jobaddress if jobaddress else "NULL"
            item["companysize"] = companysize if companysize else "NULL"
            item["companynature"] = companynature if companynature else "NULL"
            item["companyindustry"] = companyindustry if companyindustry else "NULL"

            # print item
            # print type(item)

            # with open("QC.json", "wa") as f:
            #     f.write(str(item))
                # f.write(item)

            # 存入Mongo数据库
            # db = mongo.MongodbHandeler()
            # db.process_item(item)



        except Exception, e:
            print "[ERR]: 前程数据提取失败....",
            print e
            raise


    #启动爬虫
    def run(self):

        # 翻页并提取页面当中的列表链接
        lists = self.getlinklists()
        # 获取详情页
        self.getdetailsresponse(lists)

        print "爬取成功！"



if __name__ == "__main__":

    city = raw_input("请输入城市名：")

    keyword = raw_input("请输入查询职位：")

    spider = QianChengJobSpider(city, keyword)

    # spider.getlistresponse()

    # spider.getlinklists()

    spider.run()



















