1、修改Dockerfile
![mark](http://imgs.bizha.top/bizha/20201116/5Vj96xEqInyL.png?imageslim)
SAE要求监听的端口必须在5050，修改EXPOSE为5050
![mark](http://imgs.bizha.top/bizha/20201116/tw708gIInvJF.png?imageslim)

2、开通Docker
登录Sae，控制台——云应用 SAE——创建应用（不确定开通多大可以先选个大的，后面可以缩减。）
![mark](http://imgs.bizha.top/bizha/20201116/ea5HY1mJLRU7.png?imageslim)

3、配置Git
`git init`
`git remote add sae https://git.sinacloud.com/newapp`
将修改完毕的Dockerfile复制至git文件夹。
`git add .`
`git commit -m"initial commit"`
`git push sae master:1`
PS：从新浪云服务器上删除版本1的代码。
`git push sae :1`


