##轻量级爬小说app

主要方法:vps定时执行爬虫脚本定时生成网页, 手机app打开这个网页

## 爬虫脚本

项目地址：https://github.com/specialtiger/spider

	需要：python 2.7
	原理：利用urllib2下载页面，然后正则匹配内容，将抓取的内容生成index.html
	#novel_spider.py
## 设置github网页

spider项目设置github pages，小说网页托管给github

## 服务器定时生成页面
```shell
需要：服务器 or 一台一直开着的机器
将git上的代码迁出到服务器
#crontab设置
crontab -e
#每小时的第30分钟拉取一次页面数据
10 * * * * ./home/jinxiu/code/spider/gen.sh >> /home/jinxiu/log/spider.log
#设置crontab开机启动
systemctl status crond.service #查看crontab服务状态
systemctl enable crond.service #开机自启动

#gen.sh
pwd=`dirname $0`
cd $pwd
git pull origin master
./novel_spider.py
git commit -a -m "gen index html"
git push origin
```

## 创建app

这里用apicloud创建了app，主要是方便，不用部署android开发环境。

项目地址：https://github.com/specialtiger/NovelSpiderApp/tree/master

	apicloud页面选择创建本地项目，生成的代码地址用svn工具签出
	#修改config.html, 设置app自动更新
	<preference name="autoUpdate" value="true" />
	<preference name="smartUpdate" value="true" />
	#修改index.html
	<script type="text/javascript" src="./script/api.js"></script>
	<script type="text/javascript">
	    apiready = function(){
	        //输出Log，Log将显示在APICloud Studio控制台
	        console.log("Hello APICloud");
	        api.openFrame({
	            name: 'main',
	            url: 'https://specialtiger.github.io/spider/',
	            // url: 'https://www.baidu.com',
	            bounces: true,
	            rect: {
	                x: 0,
	                y: 0,
	                w: 'auto',
	                h: 'auto'
	            }
	        });
	    };
	</script>
	</html>
​	

由于没有下载Android Studio（虽然后来下载了，但墙内用这个有点痛苦）， 考察了多个app生成方法，最后决定采用apicloud云编译。这个平台不用在本地搭建环境就可以创建app！（本来想用python for android，发现这货又是一个坑。）
最重要的是apicloud有一套线上编译发布系统，提供生成apk下载链接，已安装应用自动更新。用他的sdk可以wifi模拟器调试，由始至终不需要usb连线调试，不需要手机。
前提是要学习一点html编程基础知识。app原理是一个本地的网页框架生成的。所以看看小说足够了。需要快速的创建网页类app可以考虑一下哈。