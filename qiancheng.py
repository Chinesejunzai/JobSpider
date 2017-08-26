#coding=utf-8

import requests
from lxml import etree
import mongo

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class QianchengSpider:
    #初始化
    def __init__(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            # "Cookie": "guid=15021503299671690051; adv=adsnew%3D0%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttp%253A%252F%252Fbzclk.baidu.com%252Fadrc.php%253Ft%253D06KL00c00fZEOkb0Bs4p00uiAsaYOC9u000000IML1300000LIBnZg.THLZ_Q5n1VeHksK85yF9pywd0ZnqrHDvPjwbPhmsnj01mWbvnsKd5HuanWc3wbPawRDYwRNaPbuArRmvnDw7wjn4PWnknW7K0ADqI1YhUyPGujY1njD3rH0dPjDLFMKzUvwGujYkP6K-5y9YIZ0lQzqYTh7Wui3dnyGEmB4WUvYEIZF9mvR8TA9s5v7bTv4dUHYLrjbzn1nhmyGs5y7cRWKWwAqvHjPbnvw4Pj7PNLKvyybdphcznZufn-G4mWcsrN-VwMKpi7uLuyTq5iuo5HK-nHRzPjfzuj9Bm1bdnARdrHuBm1fvnH-WuWbsuhuB0APzm1YzPjDzP6%2526tpl%253Dtpl_10085_15730_1%2526l%253D1054828295%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%252851Job%2529-%252525E6%25252589%252525BE%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252526xp%25253Did%2528%25252522m7ad13823%25252522%2529%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D25%2526ie%253Dutf-8%2526f%253D8%2526tn%253Dbaidu%2526wd%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526rqlang%253Dcn%26%7C%26adsnum%3D789233; 51job=cenglish%3D0; search=jobarea%7E%60010000%7C%21ord_field%7E%601%7C%21recentSearch0%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1502941518%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1502150337%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21collapse_expansion%7E%601%7C%21; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D",
            "Host": "jobs.51job.com",
            "Proxy-Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        }

        # self.baseURL = "http://jobs.51job.com/beijing-dcq/93296276.html?s=01&t=0"
        self.baseURL = "http://jobs.51job.com/beijing-cyq/93306219.html?s=01&t=0"


    #爬取详情页数据
    def loadPage(self):
        response = requests.get(self.baseURL,  headers = self.headers)

        html = etree.HTML(response.content)
        # 招聘岗位
        position = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/h1/text()')[0].strip()
        print "position--",position
        # 公司名称
        company = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[1]/a/text()')[0].strip()
        print "company--",company
        # 职位月薪
        try:
            salary = html.xpath("/html/body/div[2]/div[2]/div[2]/div/div[1]/strong/text()")[0].strip()
        except:
            salary = "面议"
        # 工作地点
        # workposition = html.xpath("//div[@class = 'bmsg inbox']/p/text()")[0].strip()
        workposition = html.xpath("/html/body/div[2]/div[2]/div[3]/div[5]/div/p/text()")[1].strip()
        print "workposition--",workposition
        # 发布时间
        # releasedata = html.xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span[3]/text()')[0].strip()
        # print "releasedata--",releasedata

        #工作经验   最低学历 招聘人数 发布时间 英语 专业
        re = html.xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span/text()')
        res = "".join(re)
        #找工作经验
        index = res.find("经验")
        #找专科或是本科
        index1 = res.find("科")
        #找硕士或是博士
        index2 = res.find("士")
        #找招聘人数
        index3 = res.find("聘")
        #找发布时间
        index4 = res.find("发布")

        if index != -1:
            workbackground = res[:index+6]
            print "111111111",workposition
        else:
            workbackground = None

        if index1 != -1:
            education = res[index1 - 3:index1 + 3]
        elif index2 != -1:
            education = res[index1 - 3:index1 + 3]
        else:
            education = None

        if index3 != -1:
            if res.find("若干") != -1:
                number = 1
            else:
                number = res[index3 + 3:index3 + 4]
        else:
            number = None

        if index4 != -1:
            releasedata = res[index4 - 5:index4]
        else:
            releasedata = None







        # 工作性质
        # worknature = html.xpath("/html/body/div[6]/div[1]/ul/li[4]/strong/text()")[0].strip()
        worknature = None
        # print worknature
        # 工作经验
        # workbackground = html.xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span[1]/text()")[0].strip()
        # print "workbackground--",workbackground
        # 最低学历
        # education = html.xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span[2]/text()")[0].strip()
        # print "education--",education
        # 招聘人数
        # number = html.xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span[3]/text()")[0].strip()[2:3].encode('utf-8')

        # print "number--",number
        # 职位类别
        positioncategory = html.xpath("//div[@class = 'mt10']/p/span[@class = 'el']/text()")
        print "positioncategory--",positioncategory
        # 任职要求
        jobrequirements = html.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div/text()')
        jobrequirements_str = ''.join(jobrequirements).strip()

        # 工作地址
        jobaddress = workposition
        print "jobaddress--",jobaddress

        #公司信息
        info = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[2]/text()')[0].strip()
        info_list = info.split('|')

        # 公司性质
        companynature = info_list[0].strip()
        print "companynature--",companynature

        # 公司规模
        companysize =info_list[1].strip()
        print "companysize--",companysize

        # 公司行业
        companyindustry = info_list[2].strip()
        print "companyindustry--",companyindustry

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

            # item["position"] = position
            # item["company"] = company
            # item["salary"] = salary
            # item["workposition"] = workposition
            # item["releasedata"] = releasedata
            # item["worknature"] = worknature
            # item["workbackground"] = workbackground
            # item["education"] = education
            # item["number"] = number
            # item["positioncategory"] = positioncategory
            # item["jobrequirements"] = jobrequirements
            # item["jobaddress"] = jobaddress
            # item["companysize"] = companysize
            # item["companynature"] = companynature
            # item["companyindustry"] = companyindustry
            # item["companyhome"] = companyhome
            # item["companyaddress"] = companyaddress

            print item
            print type(item)


            # with open("qiancheng.html", "w") as f:
            #     f.write(str(item))
            #
            # # 存入Mongo数据库
            # db = mongo.MongodbHandeler()
            # db.process_item(item)



        except Exception, e:
            print "[ERR]: 前程数据提取失败....",
            print e

if __name__ == "__main__":
    spider = QianchengSpider()
    spider.loadPage()











