#coding=utf-8
#!/usr/bin/python3

import pymysql
#连接数据库
db=pymysql.connect("localhost","root","root","imageDB")
#创建游标对象
cursor=db.cursor()

#cursor.execute("drop table if exists employee")

#data=cursor.fetchone()
#创建表
# sql1="create table imageFeature(image_name char(50),object_class_code char(60),color_code text,words char(100))"
# cursor.execute(sql1)

#插入内容
sql2="insert into imageFeature(image_name,object_class_code,color_code) values('000001.jpg','(0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0)','[(139,131,137,48,240,195,371)] [(66,63,84,8,12,352,498)]')"
try:
	cursor.execute(sql2)
	db.commit()
except :
	db.rollback()

'''
#查询
sql3="select * from employee where income>'%d'"%(1000)
try:
	cursor.execute(sql3)
	results=cursor.fetchall()
	for row in results:
		fname=row[0]
		lname=row[1]
		age=row[2]
		sex=row[3]
		income=row[4]
		print("fname=%s,lname=%s,age=%d,sex=%s,income=%d"%(fname,lname,age,sex,income))
except:
	print("Error:unable to fetch data")


#更新
sql4="update employee set age = age+1 where sex='%c'"%('m')
try:
	cursor.execute(sql4)
	db.commit()
except:
	db.rollback()

#删除
sql5="delete from employee where first_name='%s'"%('fan')
try:
	cursor.execute(sql5)
	db.commit()
except:
	db.rollback()
'''
db.close()