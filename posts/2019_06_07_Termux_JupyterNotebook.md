一、Termux安装jupyter notebook

（安装前可能需要更换为国内源）
```
pkg update
pkg install proot
termux-chroot
apt install git clang
apt install pkg-config
apt install python python3-dev 
apt install libclang libclang-dev
apt install libzmq libzmq-dev
apt install ipython 
pip install jupyter
```
或者
```
pkg update
# 切换模拟的 root 环境
termux-chroot
# 安装相关依赖
pkg install libclang
# 安装 jupyter
pip3 install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
# 安装完成退出 chroot
exit
# 安装 jupyterlab
pip3 install jupyterlab -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```
二、开启局域网浏览器访问
`jupyter notebook password`
设置密码
`echo "c.NotebookApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_notebook_config.py `
开启局域网访问

三、Termux 后台运行
`nohup jupyter notebook --alow-root &`
后台运行
`lsof -i:8888`
查询运行id
`nohup kill 12234`
