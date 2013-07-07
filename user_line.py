#!/usr/bin/python
#-*-coding:utf8-*-

from web_api import conf
import docclass
from sina_master import *
import json
import os

#item {ss:dd, sd:ss}的集合
def user_line(items, sort=False):
	tl = docclass.total_classify(docclass.getWords)
	tl.setdb(conf.db_name)
	dic = tl.total_classifypercent(items)
	if sort:
		return docclass.sortedDictValues(dic)
	else:
		return dic

cache_file=r'temp.json' 

def main():
	cl = docclass.fisherclassifier(docclass.getWords)
	cl.setdb('statuses.db')
	with open("test.txt", "r") as f:
		consumer_key,consumer_secret,key,secret,userid = f.readlines()[0].strip().split(' ')
	weibo = Sina_master(consumer_key,consumer_secret)
	weibo.setToken(key, secret)
	info = weibo.get_latest_weibo(count=5, user_id="1876005872")

	with open(cache_file, 'w') as f:
		for x in info:
			print "info:%s"%x['text']
			p= cl.classifypercent(x['text'])
			print p
			f.write(json.dumps(p)+"\n")

	with open(cache_file, "rb") as f:
		dic= user_line(f.readlines())
	print sorted(dic.items(), key=lambda e:e[1], reverse=True)
	os.remove(cache_file)

if __name__ == '__main__':
	main()