# django3_test
django3官方快速入门例子使用记录


python 3.6

Django==3.0.1
mysqlclient==1.4.6

参考官方例子

使用虚拟环境

# 1、安装好对应的依赖
 
# 2、修改setting.py 数据库连接信息  创建对应的数据库

# 3、创建对应的表结构

		python manage.py makemigrations 
		python manage.py migrate


# 4、创建账号
python manage.py createsuperuser


# 5、启动
python manage.py runserver

访问url  创建好的用户登录
http://localhost:8000/admin/



# 6、集成 oauth

##		6.1在如下url中创建app
			http://localhost:8000/o/applications/
			以密码登录时 授权类型先密码
			Authorization Grant Type:password

##		6.2获取token
			
			curl --location --request POST 'http://localhost:8000/o/token/' \
			--header 'Content-Type: application/x-www-form-urlencoded' \
			--data-urlencode 'grant_type=password' \
			--data-urlencode 'client_id=UMQ4Ypnu1kWDjG043WChcEnNzSNc9kyxlH9W622d' \
			--data-urlencode 'username=admin' \
			--data-urlencode 'password=admin'
##		6.3测试url  在header中添加上认证信息 并把token类型，token放进去

			curl --location --request POST 'http://localhost:8000/api/hellot' \
			--header 'Authorization: Bearer 5EUGavCs6bJkqAMv4lODgh8J6c1Pd8' \




