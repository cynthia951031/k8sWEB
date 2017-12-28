#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

#API_URL网址
API_URL = 'http://192.168.31.85:8080/' 
BASE_URL = API_URL

class ApiClient:
	def __init__(self, base_url = BASE_URL, login_data = None):
		self.base_url = base_url
		self.login_data = login_data

	def login(self):
		if self.login_data is None:
			print 'There is no login data'
			return False
		else:
			login_url = self.base_url + 'auth'
			r = requests.post(login_url, data = self.login_data)
			if r.status_code == 200:
				self.login_cookie = dict(kubernetes_token=r.cookies['kubernetes_token'])
				print 'login success'
				return True
			else:
				print 'login failed:' + r.text
				return False


	def open(self, url, data=None, method=None):
		url = self.base_url + url
		if method == 'POST' or method == 'post':
			r = requests.post(url, data=data, cookies=self.login_cookie)
			return dict(data=r.json(), status=r.status_code)
		elif method == 'GET' or method == 'get':
			r = requests.get(url, params=data, cookies=self.login_cookie)
			return dict(data=r.json(), status=r.status_code)
		elif method == 'DELETE' or method == 'delete':
			r = requests.delete(url, data = data, cookies = self.login_cookie)
			return dict(data=r.json(), status = r.status_code)
		elif method == 'PUT' or method == 'put':
			r = requests.put(url, data=data, cookies=self.login_cookie)
			return dict(data=r.json(), status = r.status_code)
		else:
			return dict(message='method is invalide', status=400)
		return

	def get_login_cookie(self):
		login_url = self.base_url + 'auth'
		r = requests.post(login_url, data=self.login_data)
		if r.status_code == 200:
			return dict(kubernetes_token =r.cookies['kubernetes_token'])


	def create_spark(self, name, scale, cpu, memory, gpu, isSSD):
		'''
		创建一个spark实例 
		'''
		instance_name = name
		aid = 1
		param = "{\"scale\":%d,\"cpu\":%d,\"memory\":%d,\"gpu\":%d,\"isSSD\":%i}" % (scale, cpu*1000, memory, gpu, isSSD)
		data = json.dumps(dict(instance_name=instance_name, aid=aid, param=param))
		return self.open('instance', method='post', data=data)

	def delete_instance(self, iid):
		'''
		删除一个实例
		'''
		data = '{\"iid\":%d}' % iid
		return self.open('instance/' + str(iid), method='delete', data=data)['status']

	def update_instance(self, iid, new_scale):
		'''
		更新一个实例
		'''
		param = '{\"iid\":%d,\"new_scale\":%d}' %(iid, new_scale)
		data = json.dumps(dict(param=param))
		return self.open('instance/' + str(iid), method='put', data = data)['status']

	def get_instances_list(self):
		'''
		获取实例列表,参数kind为必须(all、single、proxy)
		'''
		data = dict(kind='all')
		return self.open('instance/query', method='get', data=data)['data']

	def get_instance_detail(self, iid):
		'''
		获取某个实例的详细信息，包括配置参数
		'''
		data = dict(kind='single', iid=iid)
		return self.open('instance/' + str(iid), method='get', data=data)['data']

	def get_instance_proxy(self, iid):
		'''
		获取某个实例的proxy代理链接
		'''
		data = dict(kind='proxy', iid=iid)
		return self.open('instance', method='get', data=data)['data']
