# -*- coding: utf-8 -*-

import requests

URL_IP = 'https://httpbin.org/ip'
URL_GET = 'https://httpbin.org/get'

def use_simple_requests():
	response = requests.get(URL_IP)
	print ('Reponse Headers: ',response.headers)
	print ('Reponse Body: ',response.text)


def use_params_requests():
	#构建请求参数
	params = {'param1':'hello','param2':'world'}
	#发送请求
	response = requests.get(URL_GET, params=params)
	#处理响应
	print ('Reponse Headers: ',response.headers)
	print ('Reponse Body: ',response.json())
	print ('code: ',response.status_code , response.reason)


if  __name__ == '__main__':
	print ('use simple requests')
	use_simple_requests()
	print ('user parmas requests')
	use_params_requests()