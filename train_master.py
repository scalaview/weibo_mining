#!/usr/bin/python
#-*-coding:utf8-*-

import web
import docclass
import json
from web_api.sina_dao import WebDao
from web_api import conf
from threading import Thread
from sina_master import *

urls = (
	  '/api/mining', 'Mining',
	  '/api/pro', 'Resouce',
	  '/api/traindata', 'Traindata',
    '/.*' , 'Index',
)

with open("test.txt", "r") as f:
	consumer_key,consumer_secret,key,secret,userid = f.readlines()[0].strip().split(' ')
render = web.template.render('templates')

app = web.application(urls, globals())

db = web.database(dbn="sqlite", db=conf.db_name)
cl = docclass.fisherclassifier(docclass.getWords)
cl.setdb(conf.db_name)
weibo = Sina_master(consumer_key,consumer_secret)
weibo.setToken(key, secret)
res = open(conf.pro_path).read()

class Index:
	def GET(self):
		i = web.input(pageIndex=1, pageSize=5)
		'''select id, text from statuses order by id limit ? , ?'''
		posts = db.query('select id, text from statuses where status=0 order by id limit $pageIndex , $pageSize', \
			vars={'pageIndex': i.pageIndex, 'pageSize': i.pageSize})
		count = db.select('statuses', what="count(*) c", where="status=$status", vars={'status': 0})
		print "val:%s"%count.c
		c = count.c/i.pageSize
		if (count.c%i.pageSize)!=0: c+=1
		return render.index(posts, {"count": c, "pageIndex": i.pageIndex, "pageSize": i.pageSize})

class Traindata:
	def POST(self):
		i = web.input(id=None, kind=None, content=None)
		# print i.id, i.kind, i.content
		q = db.update('statuses', where='id = $i.id', status=1, vars=locals())

		t = Thread(target=cl.train, args=(i.content, i.kind))
		t.start()
		web.header('Content-Type', 'application/json') 
		return  "succee"

class Mining:
	def GET(self):
		return render.sina_mining(userid)
	def POST(self):
		i = web.input(userid=userid, count=5)
		for x in access(weibo.get_latest_weibo, cl, i.userid, i.count):
			print x
		return render.sina_mining(userid)

class Resouce:
	def GET(self):
		web.header('Content-Type', 'application/json') 
		return res
		

def access(get_latest_weibo, classify, userid, count):
	item = dict()
	for x in get_latest_weibo(userid, count):
		print "text:%s"%x['text']
		item[x['id']] = classify.classifypercent(x['text'])
		print item[x['id']]
	return item

if __name__ == '__main__':
	app.run()