#!/usr/bin/python
#-*-coding:utf8-*-

import sqlite3 as sqlite


class WebDao():
	def __init__(self, dbfile):
		self.setdb(dbfile)

	def setdb(self,dbfile):
		self.con=sqlite.connect(dbfile, check_same_thread = False)
		self.cur = self.con.cursor()
		self.con.execute('''
create table if not exists statuses(
	id	text primary key,
	mid	text,
	text	text,
	source	text,
	favorited	integer,
	truncated	integer,
	created_at	timestamp,
	in_reply_to_status_id	text,
	in_reply_to_user_id	text,
	in_reply_to_screen_name	text,
	thumbnail_pic	text,
	bmiddle_pic	text,
	original_pic	text,
	usr_id	text,
	status  integer
)
    ''')
	def insert_or_update(self, statuse):
		count=self.count_by_id(statuse['id'])
		if count==0:
			self.cur.execute('''
				insert into statuses values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?，？)
				''', ( statuse['id'], statuse['mid'], statuse['text'], statuse['source'],\
				statuse['favorited'], statuse['truncated'], statuse['created_at'], statuse['in_reply_to_status_id'],\
				statuse['in_reply_to_user_id'], statuse['in_reply_to_screen_name'], statuse['thumbnail_pic'], \
				statuse['bmiddle_pic'], statuse['original_pic'], statuse['usr_id'], 0))
		else:
			self.cur.execute('''
			update statuses set text=?, source=? , status=? where id=?
			''', ( statuse['text'], statuse['source'], statuse['id'], 0))
		self.con.commit()

	def count_by_id(self, id):
	  res=self.cur.execute("select count(*) from statuses where id= :id ", {'id': id}).fetchone()
	  if res==None: return 0
	  else: return float(res[0])
	  self.cur.close()

	def select_all_by_separator(self, pageIndex, pageSize):
		return self.cur.execute('''select * from statuses where status=0 order by id limit ? , ?''', (pageIndex, pageSize)).fetchall()

	def select_content_by_separator(self, pageIndex, pageSize):
		return self.cur.execute('''select id, text from statuses where status=0 order by id limit ? , ?''', (pageIndex, pageSize)).fetchall()

	def close():
		self.cur.close()
		elf.con.close()