### Sublime Text 3 
Sublime Text 3  官网是`http://www.sublimetext.com/`。

### 配置
#### 1. 配置为中文。
打开软件，按`Ctrl` + `Shift` + `P`，输入`Install Package`
![](http://imgs.bizha.top//bec450cd30b1c7d4f1c8be02fef8b4d1)
输入`localiz`选择`ChineseLocalizations`
![](http://imgs.bizha.top//00456e833c77cb901d8b8b2a0c836ea9)
点击后自动安装，安装后跳出中文说明。
![](http://imgs.bizha.top//561d7a7b11aadbcd3be4f65859de784b)
即修改成了中文
![](http://imgs.bizha.top//f52fc3c9e431b4bb1254e857708afca2)

#### 2.注册or破解
![](http://imgs.bizha.top//311b8e1e24712071fd3032e6f4ce9bb5)
Sublime Text 3 可以免费无限期试用，未注册不影响使用。
注册可购买注册码。**破解**
修改`C:\Windows\System32\drivers\etc\hosts` hosts 文件
```
127.0.0.1       www.sublimetext.com
127.0.0.1       sublimetext.com
127.0.0.1       sublimehq.com
127.0.0.1       license.sublimehq.com
127.0.0.1       45.55.255.55
127.0.0.1       45.55.41.223
0.0.0.0         license.sublimehq.com
```
注册码
```
----- BEGIN LICENSE -----
Member J2TeaM
Single User License
EA7E-1011316
D7DA350E 1B8B0760 972F8B60 F3E64036
B9B4E234 F356F38F 0AD1E3B7 0E9C5FAD
FA0A2ABE 25F65BD8 D51458E5 3923CE80
87428428 79079A01 AA69F319 A1AF29A4
A684C2DC 0B1583D4 19CBD290 217618CD
5653E0A0 BACE3948 BB2EE45E 422D2C87
DD9AF44B 99C49590 D2DBDEE1 75860FD2
8C8BB2AD B2ECE5A4 EFC08AF2 25A9B864
------ END LICENSE ------
```

#### 3.配置模板。
打开软件，按`Ctrl` + `Shift` + `P`，输入`Install Package`
![](http://imgs.bizha.top//4814b6f07c2cf4f725df42b9f3d239e6)

打开插件搜索栏
![](http://imgs.bizha.top//4246f57ac717c13f703812d279c1c334)

- `SublimeTmpl `插件，快速生成文件模板。

> Ctrl+Alt+h 新建 html 文件
> Ctrl+Alt+j 新建 javascript 文件
> Ctrl+Alt+c 新建 css 文件
> Ctrl+Alt+p 新建 php 文件
> Ctrl+Alt+r 新建 ruby 文件
> Ctrl+Alt+Shift+p 新建 python 文件

在`Preferences`->`Package Settings`->`SublimeTmpl`->`Settings User`进行模板配置，如：
```
{
    "disable_keymap_actions": false, // "all"; "html,css"
    "date_format" : "%Y-%m-%d %H:%M:%S",
    "Id":"version1.2",
    "attr": {
        "author": "fuwenyue",
        "email": "fuwenyue@evip.qq.com",
        "link": "http://bizha.top",
        "Id":"version1.0"
    }
}
```
生成的文件是：
![](http://imgs.bizha.top//7e73115ef8b1d2b44b91bbfd0157fa5a)
在`SublimeTmpl\templates`文件夹中修改模板。

#### 4.安装插件
- AutoFileName
自动补全文件名插件
- Anaconda
在`Preferences`->`Package Settings`->`Anaconda`->`Settings Usert`进行模板配置。
*当前python.exe路径*
```
import sys
sys.executable
```
输出`C:\\Users\\Fuwenyue\\Anaconda3\\python.exe`。

*配置修改为`C:/Users/Fuwenyue/Anaconda3/python.exe`*

![mark](http://imgs.bizha.top/bizha/20200502/XzIjpd1lb060.png?imageslim)
```
{
	"python_interpreter": "C:/Users/Fuwenyue/Anaconda3/python.exe",
	"suppress_word_completions": true,
    "suppress_explicit_completions": true,
    "complete_parameters": true,
    "swallow_startup_errors": true,
    "anaconda_linting": false,
}
```
![mark](http://imgs.bizha.top/bizha/20200502/sdn814m7T8HG.png?imageslim)

-  OmniMarkupPreviewer
在`Preferences`→`Package Settings`→`OmniMarkupPreviewer`→`Setting——User`进行配置。
```
{
    "renderer_options-MarkdownRenderer":
    {
        "extensions": ["tables", "fenced_code", "codehilite"],
        "parser": "markdown",
        "enabled_parsers": ["markdown"]
    }
}

```
按输入快捷键：`Ctrl`+`Alt`+`O`，打开浏览器界面预览即可。
![](http://imgs.bizha.top//00b08334f216ae726a80647c67b308b4)
#### 5.查看插件列表
#### 6.移除插件






