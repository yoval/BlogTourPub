![](http://imgs.bizha.top//30de1a416e2385e2d29b28ed7076a661)
上篇是用[mlab](https://mlab.com/)提供的免费`MongoDB`数据库与Python配合，这篇是进阶使用。建立维护代理池。
爬虫思路：
### 一、获取代理，验证后导入数据库（获取）
-  1. 使用SSR代理Python，获取 socks-proxy.net 的html，解析。

使用`ProxiesCol.insert_one()`进行**添加**操作
```
LocalProxy = {'https': 'https://127.0.0.1:1080'}
Resp = requests.get(ProxyUrl,proxies = LocalProxy)
Soup = BeautifulSoup(Resp.text, 'lxml')
IpTable = Soup.select('#proxylisttable > tbody > tr')
IpList = [re.findall('<td>(.*?)</td>',str(IpRow)) for IpRow in IpTable] 
ProxiesList = [{'https':'%s://%s:%s'%(Ip[3],Ip[0],Ip[1])} for Ip in IpList]
```
- 2. 验证代理
我用的是Bilibili api验证代理，并添加地区到数据库。

`https://api.live.bilibili.com/ip_service/v1/ip_service/get_ip_addr`

![](http://imgs.bizha.top//be13d334575824f989008bc50a524071)

`SocksProxies.py`
```
IpJson = json.loads(Response.text)
country = IpJson['data']['country']
province = IpJson['data']['province']
city = IpJson['data']['city']
Proxies['Location'] = country + province + city
ProxiesCol.insert_one(Proxies)

```
导入到`MongoDB`的数据格式为：
```json
{
    "_id": {
        "$oid": "5ea930b5b1418a139229b209"
    },
    "https": "Socks4://209.13.96.172:39921",
    "Location": "阿根廷阿根廷",
    "AddTime": "2018年04月29日 15时45分57秒",
    "UpdateDate": "2018年04月29日 15时45分57秒"
}
```
### 二、从数据库获取代理并验证是否失效（维护）
- 1. 删除重复代理


```
myclient  = pymongo.MongoClient('mongodb://fuwenyue:pass4Top@ds061076.mlab.com:61076/socksproxies',retryWrites='false')
mydb = myclient['socksproxies']
ProxiesCol = mydb['unchecked']
ProxiesList = ProxiesCol.find({},{ "_id": 0, "https": 1}).sort('update',-1)
ProxiesList = [Proxies for Proxies in ProxiesList]
```
- 2. 定期校验代理。

使用 `ProxiesCol.delete_one()`、`ProxiesCol.update_one()`进行删除与更新操作，定期检查可维护代理池。

### 三、`MongoDB`的查询。

`ProxiesCol.find({},{ "_id": 0, "https": 1}).sort('update',-1)`

完整代码：https://github.com/yoval/GetSocksProxies

 


