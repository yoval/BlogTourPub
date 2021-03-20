![](http://imgs.bizha.top//e33aaa01068bc75b63d9cfea0ebdbe56)

相对于`Mysql`与`Sqlite3`数据库，`MongoDB`用起来还是很爽的，可以直接json解析，不用考虑那么多语法。甚至https://mlab.com/ 还提供500M的免费容量——还不用再本地搭建环境。
现在与python配合使用。

## 一、前期配置
### 1 .注册mlab，新建数据库、数据表。
![](http://imgs.bizha.top//4a39506ca5d92fde36a86362f5dbe0d4)
给数据库添加用户名、密码。
![](http://imgs.bizha.top//f1bdf44d96feadd295461618cd8f5fbc)
记录数据库地址
`mongodb://<dbuser>:<dbpassword>@ds253428.mlab.com:53428/tests`
`mongodb://*用户名*:*密码*@ds253428.mlab.com:53428/tests`
### 2 .安装`pymongo`
![](http://imgs.bizha.top//7bc217ab8c194f7cd12c21d543d7d3d2)

## 二、测试`pymongo`
1. 导入数据
```python
import pymongo
myclient  = pymongo.MongoClient('mongodb://fuwenyue:pass4Top@ds253428.mlab.com:53428/tests',retryWrites='false')
mydb = myclient['tests'] # 连接数据库
myCol = mydb['Proxies'] # 连接or创建数据表
data = {'中国':'13亿','美国':'4亿'} # 需要导入的数据
x = myCol.insert_one(data) # 向数据表插入数据
print(x)
```
print 的结果
><pymongo.results.InsertOneResult object at 0x000001AECE1FFFC8>

导入成功
![](http://imgs.bizha.top//b17bab6f81a31bcf5389e0cb9f177cb6)

2. 读取数据
```python
import pymongo
myclient  = pymongo.MongoClient('mongodb://fuwenyue:pass4Top@ds253428.mlab.com:53428/tests',retryWrites='false')
mydb = myclient['tests'] # 连接数据库
myCol = mydb['Proxies'] # 连接or创建数据表
data = myCol.find()
print(data[0])

```
print的结果是：
```
{'_id': ObjectId('5ea902fb61e7a1aea569cc34'), '中国': '13亿', '美国': '4亿'}
```
读取成功

3. 删除数据
```python
import pymongo
myclient  = pymongo.MongoClient('mongodb://fuwenyue:pass4Top@ds253428.mlab.com:53428/tests',retryWrites='false')
mydb = myclient['tests'] # 连接数据库
myCol = mydb['Proxies'] # 连接or创建数据表
data = myCol.find()[0]
y = myCol.delete_one(data)
print(y)
```
print结果是
><pymongo.results.DeleteResult at 0x1aecd580a88>

![](http://imgs.bizha.top//fad2c0db8a17a45740bbe4560ae826f9)
删除成功！
