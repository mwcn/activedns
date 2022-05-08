#author: wenyaohui
#email: i@mue.cx
#time: 2022/5/1
#website: mue.cx
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models

while 1:
    # 开局先读取上一次ip进内存
    f = open("ip.txt", "r")
    str = f.read()

    # 这次的ip，获取到后再写入
    file_handle = open('ip.txt', mode='r+')
    f = os.popen("curl -ss ipinfo.io/ip")  #这里ifconfig.me可以换 参考https://mue.cx/2022/88f44ab99bd9.html网站
    a = f.read().strip()
    print(a)
    file_handle.write(a)
    # 对两次ip进行判断
    if a == str:
        print('IP相同，解析正常')
    else:
        print('公网IP已变更，正在修改解析···')
        import json
        import os
        import time

        from tencentcloud.common import credential
        from tencentcloud.common.profile.client_profile import ClientProfile
        from tencentcloud.common.profile.http_profile import HttpProfile
        from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
        from tencentcloud.dnspod.v20210323 import dnspod_client, models

        f = open('config.txt', 'r')
        line = f.readlines()
        SecretId = line[0].strip('SecretId = \n')
        SecretKey = line[1].strip('SecretKey = \n')

        # SecretId = SecretId
        # SecretKey = 'JRUL3YqujEXbQ1Qq56tSnvoUv7D8pIWW'

        try:
            # 输出全部域名测试
            cred = credential.Credential(SecretId, SecretKey)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "dnspod.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = dnspod_client.DnspodClient(cred, "", clientProfile)

            req = models.DescribeDomainListRequest()
            params = {

            }
            req.from_json_string(json.dumps(params))

            resp = client.DescribeDomainList(req)

            resp_dict = json.loads(resp.to_json_string())

            num = resp_dict['DomainCountInfo']['DomainTotal']

           # for i in range(num):
               # print(resp_dict['DomainList'][i]['Name'])
            print("域名列表列出成功 API通信正常")
            print("------------------------------")
            time.sleep(1)
            # 删除记录
            req = models.DeleteRecordRequest()
            f = open("delrecord.txt", "r")
            str2 = f.read()
            f.close()
            f = open('recordi.txt', 'r')
            line = f.readlines()
            domain = line[0].strip()
            f.close()
            params = {
                "Domain": domain,
                "RecordId": int(float(str2))
            }

            req.from_json_string(json.dumps(params))

            resp = client.DeleteRecord(req)
            print("删除原记录成功")


        except TencentCloudSDKException as err:
            pass
            print(err)
        finally:
            req = models.CreateRecordRequest()

            f = open('recordi.txt', 'r')
            line = f.readlines()
            domain = line[0].strip()
            zdomain = line[1].strip()
            jxtype = line[2].strip()
            #jxvalue = line[3].strip()
            # print(jxvalue)
            f.close()

            params = {
                "Domain": domain,
                "SubDomain": zdomain,
                "RecordType": jxtype,
                "RecordLine": "默认",
                "Value": a
            }
            req.from_json_string(json.dumps(params))

            resp = client.CreateRecord(req)

            resp_dict = json.loads(resp.to_json_string())
            print("新增解析成功")
            del str
            file_handle = open('delrecord.txt', mode='r+')
            f = resp_dict['RecordId']  # 这里ip.sb可以换 参考xxxx网站
            b = str(f)
            file_handle.write(b)
            file_handle.close()
        time.sleep(8)
        #开始执行修改解析操作

    continue
