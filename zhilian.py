#coding=utf-8

import requests
from lxml import etree
import mongo
# from mongo import *




import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ZhilianSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        }

        self.baseURL = "http://jobs.zhaopin.com/275470883250186.htm?ssidkey=y&ss=201&ff=03&sg=496b26b603284454b68ca394b1a88216&so=5"
        # self.baseURL = "http://sou.zhaopin.com/jobs/searchresult.ashx?"
        # self.positionName = raw_input("请输入需要抓取的职位名:")
        # self.cityName = raw_input("请输入需要抓取的城市名:")
        # self.endPage = int(raw_input("请输入需要抓取的页数:"))


    def loadPage(self):

        response = requests.get(self.baseURL,headers = self.headers)
        # print type(response.content)

        html = etree.HTML(response.content)
        # print type(html)
        #招聘岗位
        position = html.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()')[0].strip()
        # print position
        #公司名称
        company = html.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/text()')[0].strip()
        # print company
        #职位月薪
        salary = html.xpath("/html/body/div[6]/div[1]/ul/li[1]/strong/text()")[0].strip()[:-3].encode("utf-8")

        print salary
        print type(salary)

        # print type()
        #工作地点
        workposition = html.xpath("/html/body/div[6]/div[1]/ul/li[2]/strong/a/text()")[0].strip()
        # print workposition
        #发布时间
        releasedata = html.xpath('//*[@id="span4freshdate"]/text()')[0].strip()
        # print releasedata
        #工作性质
        worknature = html.xpath("/html/body/div[6]/div[1]/ul/li[4]/strong/text()")[0].strip()
        # print worknature
        #工作经验
        workbackground = html.xpath("/html/body/div[6]/div[1]/ul/li[5]/strong/text()")[0].strip()
        # print workbackground
        #最低学历
        education = html.xpath("/html/body/div[6]/div[1]/ul/li[6]/strong/text()")[0].strip()
        # print education
        #招聘人数
        number = int(html.xpath("/html/body/div[6]/div[1]/ul/li[7]/strong/text()")[0].strip()[:-1].encode("utf-8"))

        print number
        print type(number)
        #职位类别
        positioncategory = html.xpath("/html/body/div[6]/div[1]/ul/li[8]/strong/a/text()")[0].strip()
        # print positioncategory
        #任职要求
        jobrequirements = html.xpath('//div[@class = "tab-inner-cont"]/p/text()')[:-4]
        # print len(jobrequirements)
        # print type(jobrequirements)
        # print "===============",jobrequirements
        # for i in jobrequirements:
        #     print i
        #工作地址
        jobaddress = html.xpath('//div[@class = "tab-inner-cont"]/h2/text()')[0].strip()
        # print "+++++++++++++++",jobaddress

        #公司规模
        companysize = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[1]/strong/text()')[0].strip()
        # print "*****************",companysize

        #公司性质
        companynature = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[2]/strong/text()')[0].strip()
        # print "1111111111111111",companynature

        #公司行业
        companyindustry = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[3]/strong/a/text()')[0].strip()
        # print "2222222222222222222", companyindustry

        #公司主页链接

        companyhome = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[4]/strong/a/@href')[0].strip()
        print "33333333333333",companyhome


        #公司地址

        companyaddress = html.xpath('/html/body/div[6]/div[2]/div[1]/ul/li[5]/strong/text()')[0].strip()
        # print "44444444444444", companyaddress
        try:
            #将数据封装为字典形式进行存储
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

            #存入Mongo数据库
            db = mongo.MongodbHandeler()
            db.process_item(item)

        except Exception, e:
            print "[ERR]: 智联数据提取失败....",
            print e
            raise



# print response.text


if __name__ == "__main__":
    spider = ZhilianSpider()
    spider.loadPage()







