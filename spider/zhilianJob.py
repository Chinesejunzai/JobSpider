#!/usr/bin/env python
# encoding=utf-8


'''

@author: caopeng

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: Chinesejunzai@163.com

@software: garner

@file: zhilianJob.py

@time: 17-8-23 上午9:47

@desc:

'''


import requests
import urllib
from lxml import etree
# from selenium import webdriver
# from time import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ZhiLianJobSpider:
    def __init__(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Cookie": "LastCity=%e5%8c%97%e4%ba%ac; LastCity%5Fid=530; JSSearchModel=0; __xsptplus30=30.6.1502272314.1502272314.1%234%7C%7C%7C%7C%7C%23%23xueaEIonEhsNl2emlJhK5rGC9LOQmOYV%23; zg_did=%7B%22did%22%3A%20%2215dcb972cf31-015711f4fb975d-6315107d-100200-15dcb972cf43c%22%7D; zg_08c5bcee6e9a4c0594a5d34b79b9622a=%7B%22sid%22%3A%201502359268602%2C%22updated%22%3A%201502359268602%2C%22info%22%3A%201502359268608%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22sou.zhaopin.com%22%7D; utype=667215829; rt=97d6929bf2134a71a9ad8c5420ef7d20; dywez=95841923.1502976080.25.10.dywecsr=mail.126.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/js6/read/readhtml.jsp; _jzqx=1.1496028809.1502976081.2.jzqsr=zhaopin%2Ecom|jzqct=/.jzqsr=mail%2E126%2Ecom|jzqct=/js6/read/readhtml%2Ejsp; _qzja=1.465078639.1498558711577.1502959955399.1503026234820.1503026234820.1503026304066.0.0.0.19.10; _jzqa=1.3766657437477915000.1496028809.1503020439.1503026232.19; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1503020439,1503026232,1503322221,1503453646; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1503453646; __utmt=1; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e9%a4%90%e8%a1%a5%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e5%8c%85%e5%90%83%7c%e5%8c%85%e4%bd%8f%7c%e6%88%bf%e8%a1%a5%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4; LastSearchHistory=%7b%22Id%22%3a%22abb43eb1-f5d3-4e98-917e-f88921881fa2%22%2c%22Name%22%3a%22python+%2b+%e5%8c%97%e4%ba%ac+%2b+%e6%9c%80%e8%bf%91%e4%b8%80%e5%91%a8%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e5%258c%2597%25e4%25ba%25ac%26kw%3dpython%26sm%3d0%26isfilter%3d1%26p%3d1%26pd%3d7%22%2c%22SaveTime%22%3a%22%5c%2fDate(1503454413530%2b0800)%5c%2f%22%7d; dywea=95841923.3718908553051214000.1495372313.1503322221.1503453646.29; dywec=95841923; dyweb=95841923.11.9.1503454410123; __utma=269921210.355485063.1495372314.1503322222.1503453646.29; __utmb=269921210.11.9.1503454410126; __utmc=269921210; __utmz=269921210.1502976080.25.10.utmcsr=mail.126.com|utmccn=(referral)|utmcmd=referral|utmcct=/js6/read/readhtml.jsp; BLACKSTRIP=yes",
            # "Host": "sou.zhaopin.com",
            # "Proxy-Connection": "keep-alive",
            "Referer":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        }

        self.baseURL = "http://sou.zhaopin.com/jobs/searchresult.ashx"
        # self.driver = webdriver.Chrome()
        # self.num = 1


    name = "zl_job"

    def loadlistpage(self):
        #查询参数
        zlgw_params = {
            "pd": "7",  # 发布时间
            "jl": "北京",  # 地区
            "kw": "python",  # 搜索条件
            "sm": "0",
            "p": "1",
            "sf": "0",
            "st": "99999",
            "isadv": "1"
        }

        # zlgw_params['pd'] = params['pub_date']
        # zlgw_params['jl'] = params['location']
        # zlgw_params['kw'] = params['position']
        i = 1
        while True:

            html = etree.HTML(response.content)
            linkempty = html.xpath('//a[@class="next-page"]/@href')[0]

            if linkempty != "NULL":
                try:
                    response = requests.get(self.baseURL, params=zlgw_params, headers = self.headers)
                except Exception, e:
                    print "************timeout***************"
                    print e


                link_list = html.xpath('//div[@class = "newlist_list_content"]/table/tr/td/div/a/@href')

                print link_list
                zlgw_params["p"] = i+1


            else:
                break



    # def loadlistpage(self):
    #     # 查询参数
    #     # zlgw_params = {
    #     #     "pd": "7",  # 发布时间
    #     #     "jl": "北京",  # 地区
    #     #     "kw": "python",  # 搜索条件
    #     #     "sm": "0",
    #     #     "p": "1",
    #     #     "sf": "0",
    #     #     "st": "99999",
    #     #     "isadv": "1"
    #     # }
    #     try:
    #         response = requests.get(self.baseURL, headers = self.headers)
    #     except Exception, e:
    #         print "************timeout***************"
    #         print e
    #     return response.content
    #
    #
    # def dealPage(self, html):
    #
    #     # self.driver.get(self.baseURL)
    #
    #     # print html
    #
    #     lists = []
    #     # print type(str(self.driver.page_source))
    #
    #     while True:
    #         # html = str(self.driver.page_source)
    #         # with open("11.html", "w") as f:
    #         #     f.write(html)
    #
    #         html = etree.HTML(html)
    #         print html
    #         #获取详情页的链接
    #         link_list = html.xpath('//div[@class = "newlist_list_content"]/table/tr/td/div/a/@href')
    #         link_list = html.xpath('//*[@id="newlist_list_content_table"]/dtable/tbody/tr[1]/td[1]/div/a/@href')
    #         print len(link_list)
    #         print link_list
    #
    #         # el_list = self.driver.find_elements_by_xpath('//*[@id="newlist_list_content_table"]/table/tbody/tr[1]/td[1]/div/a')
    #         #
    #         # for el in el_list:
    #         #     a_list = el.get_attribute('href')
    #         #     lists.append(a_list)
    #         # self.num += 1
    #         print lists
    #
    #         #不等于-1,就是找到了,到最后一页了,
    #         #等于-1,就是没找到,说明没到最后一页
    #     #     if self.driver.page_source.find("next-page nopress2") != -1:
    #     #         break
    #     #
    #     #     self.driver.find_element_by_xpath("//a[@class='next-page']").click()
    #     #     time.sleep(1)
    #     #
    #     # print lists
    #     # print "\n" + str(self.num)
    #     # self.driver.quit()


if __name__ == "__main__":

    spider = ZhiLianJobSpider()
    spider.loadlistpage()
    # spider.dealPage(response)










