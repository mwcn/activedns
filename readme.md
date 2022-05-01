# activedns

自身需求做的一个小功能，本项目为解决公网ip变更的问题，只需将本项目screen挂置系统后台运行在服务端即可，windows下内存占用约6M左右
使用前提：自备一个腾讯云帐号，一个域名(可以.top域名，几块钱一年)

## 实现功能：

1. 挂置客户端实时获取本地公网IP是否变更
2. 若本地IP变更则立即修改腾讯云域名解析的记录值

## 参数配置：
1. config.txt 该文件为域名配置文件，SecretId，SecretKey需登录腾讯云访问管理处生成。（登录腾讯云后访问https://console.cloud.tencent.com/cam/capi）

![image-20220501180609230](https://mue.cx/images/image-20220501181609345.png)

这里我打了星号，从腾讯云api管理处获取到的是完整的，自行填写完整id与key

1. recordi.txt 该文件为解析配置文件
    第一行填写一级域名，第二行填写子域名，第三行填写解析类型(实际上针对ip进行解析大部分使用还是a记录，这里就不写死了)，记录值默认是你本机的公网ip
2. 其他txt文件不用管，代码取数据用的

## 使用方法：

`pip install tencentcloud-sdk-python`

`pip install json`

`python index.py`

## 项目说明：

1. 本项目运行于python3.10，其的配置文件中的参数所处行不可变更，否则无法正常运行
1. 首次执行，若报错，则再执行一次
1. 目前正在测试中，挂置期间，不能断网，断网程序就挂了。 可以跑定时任务，定时执行该文件

## 捐赠

B站充电以便我更好的跑路
https://space.bilibili.com/1887506718
