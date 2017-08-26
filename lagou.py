#coding=utf-8

import requests
from lxml import etree
import mongo

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class LaGouSpider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",}

        self.baseURL = "https://www.lagou.com/jobs/3409443.html"
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
        position = html.xpath('/html/body/div[2]/div/div[1]/div/span/text()')[0].strip()
        print position
        #公司名称
        company = html.xpath('//*[@id="job_company"]/dt/a/div/h2/text()')[0].strip()
        print company
        #职位月薪
        salary = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[1]/text()")[0].strip()
        print salary
        #工作地点
        workposition1 = html.xpath("//*[@id='job_detail']/dd[3]/div[1]/a/text()")[:-1]
        workposition1 = ''.join(workposition1)
        workposition2 = html.xpath("//*[@id='job_detail']/dd[3]/div[1]/text()")
        workposition2 = ''.join(workposition2)
        workposition2 = workposition2.split('-')
        workposition2 = ''.join(workposition2).strip()
        workposition = workposition1 + workposition2
        print workposition
        #发布时间
        releasedata = html.xpath('/html/body/div[2]/div/div[1]/dd/p[2]/text()')[0].strip()
        print releasedata
        #工作性质
        worknature = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[5]/text()")[0].strip()
        print worknature
        #工作经验
        workbackground = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[3]/text()")[0].strip()
        print workbackground
        #最低学历
        education = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[4]/text()")[0].strip()
        print education
        #招聘人数
        number = 1
        print number
        #职位类别
        positioncategory = html.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[5]/text()")[0].strip()
        print positioncategory
        #任职要求
        jobrequirements = html.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')
        jobrequirements_str = ''.join(jobrequirements).strip()
        # print len(jobrequirements)
        # print type(jobrequirements)
        # print "===============",jobrequirements_str
        for i in jobrequirements:
            print i
        #工作地址
        jobaddress = workposition
        print "+++++++++++++++",jobaddress

        #公司规模
        companysize = html.xpath('//*[@id="job_company"]/dd/ul/li[3]/text()')[1].strip()
        print "*****************",companysize

        #公司性质  发展阶段
        companynature = html.xpath('//*[@id="job_company"]/dd/ul/li[2]/text()')[1].strip()
        print "1111111111111111",companynature

        #公司行业
        companyindustry = html.xpath('//*[@id="job_company"]/dd/ul/li[1]/text()')[1].strip()
        print "2222222222222222222", companyindustry

        #公司主页链接
        try:
            companyhome = html.xpath('//*[@id="job_company"]/dd/ul/li/a/@href')[0].strip()
        except:
            companyhome = None
        print "33333333333333",companyhome

        #公司地址
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
            with open("zhao.json", "w") as f:
                f.write(str(item))

            # 存入Mongo数据库
            db = mongo.MongodbHandeler()
            db.process_item(item)


        except Exception, e:
            print "[ERR]: 拉勾数据提取失败....",
            print e



if __name__ == "__main__":
    spider = LaGouSpider()
    spider.loadPage()







