# DomainWhois爬虫

通过分析官网`nic.top`，可知查询原理是`post`    域名到`http://www.nic.top/cn/whoischeck.asp`。
![](http://imgs.bizha.top//48b881700ae6b2c2427294ed6504133c)
`Form Data`为
![](http://imgs.bizha.top//840ee211344c6546cae7ae8c546d249e)

所以python代码为
```python
import requests

Url = 'http://www.nic.top/cn/whoischeck.asp'
Data = {'domainName': 'bizha'}

rep = requests.post(Url,Data)
```

也可以通过`WHOIS Server`获取。
```python
import socket
domain = b'bizha.top\n'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('whois.nic.top',43))
s.send(domain)
v = s.recv(10240)
```


完整代码：
github：`https://github.com/yoval/DomainWhois`




