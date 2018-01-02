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
			return False
		else:
			login_url = self.base_url + 'user/auth'
			r = requests.post(login_url, json=self.login_data)
			if r.status_code == 200:
				self.login_cookie = dict(kubernetes_token=r.cookies['kubernetes_token'])
				return True
			else:
				return False

	def open(self, url, data = None, method = None):
		url = self.base_url + url
		if method == 'POST':
			r = requests.post(url, json = data, cookies=self.login_cookie)
			return dict(data = r.json(), status=r.status_code)
		elif method == 'GET':
			r = requests.get(url, json = data, cookies=self.login_cookie)
			return dict(data = r.json(), status=r.status_code)
		elif method == 'DELETE':
			r = requests.delete(url, json = data, cookies = self.login_cookie)
			return dict(data = r.json(), status = r.status_code)
		elif method == 'PUT':
			r = requests.put(url, json = data, cookies=self.login_cookie)
			return dict(data = r.json(), status = r.status_code)
		else:
			return dict(message='method is invalide', status=400)
		return

	def create_instance(self, name, scale, cpu, memory, gpu, isSSD):
		instance_name = name
		aid = 1
		param = dict(scale = scale, cpu = cpu * 1000, memory = memory, gpu = gpu, isSSD = isSSD)
		data = json.dumps(dict(instance_name=instance_name, aid=aid, param=param))
		return self.open('instance', method = 'POST', json = data)['status']

	def delete_instance(self, iid):
		data = dict(iid = iid)
		return self.open('instance/' + str(iid), method = 'DELETE', json = data)['status']

	def update_instance(self, iid, new_scale):
		param = dict(new_scale = new_scale)
		data = json.dumps(dict(param=param))
		return self.open('instance/' + str(iid), method = 'PUT', json = data)['status']

	def get_instances_list(self):
		data = dict(kind='all')
		return self.open('instance/query', method = 'GET', json = data)['data']

	def get_instance_detail(self, iid):
		data = dict(kind = 'single', iid = iid)
		return self.open('instance/' + str(iid), method = 'GET', json = data)['data']
	'''
	def get_instance_proxy(self, iid):
		#获取某个实例的proxy代理链接
		data = dict(kind='proxy', iid=iid)
		return self.open('instance', method='get', data=data)['data']
	'''