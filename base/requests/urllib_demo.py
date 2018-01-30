# -*- coding: utf-8 -*-

import urllib
import urllib.request
import urllib.parse

URL_IP = 'https://httpbin.org/ip'
URL_GET = 'https://httpbin.org/get'

def use_simple_urllib():
	response = urllib.request.urlopen(URL_IP)
	print ('Reponse Headers: ',response.info())
	print ('text: ',response.read())


def use_params_urllib():
	#构建请求参数
	params = urllib.parse.urlencode({'param1':'hello','param2':'world'})
	print ('Request params: ', params)
	#发送请求
	response = urllib.request.urlopen('?'.join([URL_GET, '%s']) % params)
	#处理响应
	print ('Reponse Headers: ',response.info())
	print ('text: ',response.read().decode('utf-8'))
	print ('code: ',response.getcode())


if  __name__ == '__main__':
	print ('use simple urllib')
	use_simple_urllib()
	print ('user parmas urllib')
	use_params_urllib()