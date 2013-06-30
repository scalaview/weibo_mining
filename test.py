#!/usr/bin/python
#-*-coding:utf8-*-

from sina_master import *
import json
import chardet
import jieba
import re
import docclass
import string

# def test():
	# print docclass.getwords("aaa,bbb,vvv,ddd,eee,ddd,ffff,ddd,ddd,sss,aaa,aaa,ddd")
extra_punctuation="，。“”＂！、‘’（）@#￥%……&*——+=： "
def main():
	# table = string.maketrans("","")
	s = '从满脸痘痘到细腻皮肤的蜕变，大S及皮肤科医生都推荐的修复面膜，[ 围观]解决皮肤的多种问题~点击查看详情：http://t.cn/zHFnve4'
	for x in getWords(s):
		print x
	# s.translate(table, string.punctuation+extra_punctuation)
	# regxs = {r'\[\S+?\]': ''}
	# for key,value in regxs.items():
	# 	print key, value
	# with open("test.txt", "r") as f:
		# consumer_key,consumer_secret,key,secret,userid = f.readlines()[1].strip().split(' ')
	# print consumer_key,consumer_secret,key,secret,userid
	# run_crawler(consumer_key,consumer_secret,key,secret,userid)
	# weibo = Sina_master(consumer_key,consumer_secret)
	# weibo.setToken(key, secret)
	# weibo.manage_access()
	# info = weibo.get_latest_weibo(count=5, user_id=userid)
	# reptile(sina_reptile,userid)
	# sina_reptile.connection.close()
	# for x in info:
	# 	print x
	# 	print x['geo']['city']
		# print x['text']
		# words =getWords(x['text'])
		# # print x['text']
		# cl = docclass.fisherclassifier(getWords)
		# cl.setdb('test.db')
		# print cl.cprob('幸福', 'test')
		# print cl.fisherprob('幸福', 'test')
		# cl.train(x, 'test;up;kill;volite')
		# print cl.classifypercent('故事的结尾是周公子和易烨卿幸福地生活在一起么')
		# print ','.join(jieba.cut(x['text']))
		# print words, _mood
		# for t in words:
		# 	print t
		# encodedjson = json.dumps(x)
		# for y in encodedjson:
		# 	print "%s: %s\n"% (y, encodedjson[y].encode('utf8'))
		# text = x['text']
		# for i in re.findall(r'\[\S+?\]',x['text'].decode('utf-8')):  
			# print 'data:' +i  #心情表情
			# _mood.add(i)
			# text = text.replace(i, '')
                 # if d.has_key(data):  
                 #     if cols[14]=='f':  
                 #         d[data][0]+=1 
                 #         d[data][2]+=1 
                 #     else:  
                 #         d[data][1]+=1 
                 #         d[data][2]+=1 
                 # else:  
                 #     if cols[14]=='f':  
                 #         d[data]=[1,0,1]  
                 #     else:  
                 #         d[data]=[0,1,1] 
		# print ','.join(jieba.cut(text))
		# print chardet.detect(x['retweeted_status'])
		# print chardet.detect(x['geo'])

	# print info
	# with open("data.txt", 'w') as f:
	# 	for x in info:
	# 		f.write("%s\n" % x)
	# 
	# test()

def getWords(doc):
	# _mood = set()
	# for i in re.findall(r'\[\S+?\]',doc.decode('utf-8')):  
	# 	# print 'data:' +i  #心情表情
	# 	_mood.add(i)
	# 	doc = doc.replace(i, '')
	# return dict([(w,1) for w in jieba.cut(doc)])
	# _mood = set()
	# regxs = {r'\[\S+?\]': '', r'//@.*:': ''}
	# for key,value in regxs.items():
	# 	print "pre:%s"%doc
	# 	doc = re.sub(key, value, doc, flags=re.IGNORECASE)
	# 	print "aft:%s"%doc
	# return dict([(w,1) for w in jieba.cut_for_search(doc)])
	_mood = set()
	regxs = {r'\[.*\]': '', r'//@.*:': ''}
	for key,value in regxs.items():
	  # print "pre:%s"%doc
	  doc = re.sub(key, value, doc.decode('utf8'), flags=re.IGNORECASE)
	  # print "aft:%s"%doc
	# table = string.maketrans("", "")
	# doc.translate(table, string.punctuation)
	regex = re.compile('[%s]' % re.escape(string.punctuation))
	doc = regex.sub('', doc)
	print "reg:%s" % doc
	res = dict()
	for w in jieba.cut_for_search(doc):
		if w in string.punctuation+extra_punctuation or len(w)<2:
			print "s", w
		else:
			res[w] =1
	return res

if __name__ == '__main__':
	main()