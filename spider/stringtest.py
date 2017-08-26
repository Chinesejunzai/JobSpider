#!/usr/bin/env python
# encoding=utf-8

'''

@author: houxiaojun

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: Chinesejunzai@163.com

@software: garner

@file: stringtest.py

@time: 17-8-25 下午6:25

@desc:

'''

# re = html.xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span/text()')
# res = "".join(re)
res = "  2年经验本科招聘1人08-25发布   "

# index = a.find("经验")
# print index
# b = a[:index+6]
# print b
#
# index1 = a.find("科")
# print index1
# d = a[index1-3:index1+3]
# print "111111",d

# index2 = a.find("聘")
# print index2
# e = a[index2+3:index2+4]
# print e

# if index1:
#     if a.find("若干"):
#         c = 1
#     else:
#         c = a[index1+6:index1+7]
#     print c
# else:
#     print "没找到"
#
# index2 = a.find("发布")
# # print index2
#
# d = a[index2-5:index2]
# print d

# 找工作经验
index = res.find("经验")
# 找专科或是本科

index1 = res.find("科")
index11 = res.find("专")
print index11
education = res[index1 - 3:index1 + 3]
print "-----", education
# 找硕士或是博士
index2 = res.find("士")
# 找招聘人数
index3 = res.find("聘")
# 找发布时间
index4 = res.find("发布")

# 工作经验
if index != -1:
    workbackground = res[:index + 6]
    print "workbackground--", workbackground
else:
    workbackground = None
    print "workbackground--", workbackground

# 专科或是本科  硕士或是博士
if index1 != -1:
    education = res[index1 - 3:index1 + 3]
    print "education--", education
elif index2 != -1:
    education = res[index2 - 3:index2 + 3]
    print "education++", education
elif index11 != -1:
    education = res[index11 - 3:index11 + 3]
    print "education1111", education
else:
    education = None
    print "education==", education

# 招聘人数
if index3 != -1:
    if res.find("若干") != -1:
        number = 1
        print "number--", number
    else:
        number = res[index3 + 3:index3 + 4]
        print "number++", number
else:
    number = None
    print "number==", number

# 发布时间
if index4 != -1:
    releasedata = res[index4 - 5:index4]
    print "releasedata--", releasedata
else:
    releasedata = None
    print "releasedata++", releasedata





