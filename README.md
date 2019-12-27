# django3_test
django3官方快速入门例子使用记录


python 3.6

Django==3.0.1
mysqlclient==1.4.6

参考官方例子

使用虚拟环境

# 1、安装好对应的依赖
 
#2、修改setting.py 数据库连接信息  创建对应的数据库

#3、创建对应的表结构

		python manage.py makemigrations 
		python manage.py migrate


#4、创建账号
python manage.py createsuperuser


#5、启动
python manage.py runserver

访问url  创建好的用户登录
http://localhost:8000/admin/



