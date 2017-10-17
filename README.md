## 爬虫脚本

## 定时生成并提交页面
```shell
#crontab设置
crontab -e
#每小时的第30分钟拉取一次页面数据
10 * * * * ./home/jinxiu/code/spider/gen.sh >> /home/jinxiu/log/spider.log
systemctl restart crond.service # 重启服务
systemctl reload crond.service #重新载入配置
systemctl status crond.service #查看crontab服务状态
systemctl enable crond.service #开机自启动

```
## 创建app
由于没有下载Android Studio（虽然后来下载了，但墙内用这个有点痛苦）， 考察了多个app生成方法，最后决定采用apicloud云编译。这个平台居然不用在本地搭建环境就可以创建app！（本来想用python for android，发现这货又是一个坑。）
最重要的是apicloud有一套线上编译发布系统，提供生成apk下载链接，已安装应用自动更新。用他的sdk可以wifi模拟器调试，由始至终不需要usb连线调试，不需要手机。
前提是要学习一点html编程基础知识。app原理是一个本地的网页框架生成的。所以看看小说足够了。需要快速的创建网页类app可以考虑一下哈。