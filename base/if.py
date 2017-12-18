# -*- coding: utf-8 -*-

#elif是else if的缩写

#小明身高 1.75，体重 80.5kg。请根据 BMI 公式（体重除以身高的平方）帮小明计算他的 BMI 指数，并根据 BMI 指数： 
#   低于 18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于 32：严重肥胖

s = input('输入体重：')
weight = float(s)
if weight < 18.5:
	print ("过轻")
elif weight >= 18.5 and weight < 25:
	print ("正常")
elif weight >= 25 and weight < 28:
	print ("过重")
elif weight >= 28 and weight < 32:
 	print ("肥胖")
else:
 	print ("严重肥胖")