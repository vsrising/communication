# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 06:47:49 2021

@author: Administrator
"""

ids=["1370282855070044160", "1370282334183624704", "1370281323352166400", "1370279575266922496", "1370272330311405568", "1370272175965212672", "1370258326901886976", "1370258170651480064", "1370257950492463104", "1370206416350089216", "1370206278575591424", "1370198400431165440", "1370198027322658816", "1370197802721873920", "1370197651722735616", "1370178608169095168", "1370170990490947584", "1370006962099589120", "1370006684243726336", "1370006581546192896", "1370006417787981824", "1370006282811084800", "1370006171225821184", "1370006065449668608", "1369927008364138496", "1369916646008950784", "1369901010377641984", "1369900785709748224", "1369900461758484480", "1369875207233343488", "1369875030950940672", "1369874860892884992", "1369874463830708224", "1369873982811148288", "1369839908583247872", "1369839492340518912", "1369822128714682368", "1369813835082502144", "1369811881702854656", "1369811660587536384", "1369810902479671296", "1369810822020337664", "1369810733679906816", "1369810610279288832", "1369601745285681152", "1369601445720100864", "1369601283467644928", "1369600880189509632", "1369600798656434176", "1369600656645689344", "1369560684437835776", "1369559631705280512", "1369559338955444224", "1369532121022074880", "1369531944383156224", "1369479328542363648", "1369478682086871040", "1369460765618212864", "1369448274431447040", "1369298824220250112", "1369298617189404672", "1369298292629966848", "1369297965545558016", "1369259851947053056", "1369217151076012032", "1369216919630123008", "1369180402979311616", "1369180242962419712", "1369147691464003584", "1369145018635390976", "1369144860577239040", "1369144209432514560", "1369143996387037184", "1369143836839907328", "1369143710343892992"]
import requests
import time 
url="https://mt.fjii.com/api/wechatShareTask/shareSum"

#payload="{\"isLoadTip\":\"...\",\"user_id\":\"1316927879329746944\",\"wechat_share_task_id\":\"1414761988562751488\",\"type\":2,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
headers={
'POSThttps':'//mt.fjii.com/api/wechatShareTask/shareSumHTTP/1.1',
'Host':'mt.fjii.com',
'Connection':'keep-alive',
'Content-Length':'302',
'Accept':'application/json,text/plain,*/*',
'User-Agent':'Mozilla/5.0(Linux;Android10;ALP-AL00Build/HUAWEIALP-AL00;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/83.0.4103.106MobileSafari/537.36wpsystem',
'Content-Type':'application/json;charset=UTF-8',
'Origin':'https://mt.fjii.com',
'X-Requested-With':'com.fuzhou.wpsystem',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':'token=35d0327a-b5f0-4a26-94bb-18aec8a546e1'
}

payload="{\"isLoadTip\":\"...\",\"user_id\":\"1316927879329746944\",\"wechat_share_task_id\":\""
#for i in range(173740533760,973740533760):
nums=1
for i in ids:
    #id="1414915"+str(i)    
    end1="\",\"type\":1,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads1=payload+i+end1
    
    end2="\",\"type\":2,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads2=payload+i+end2
    
    end3="\",\"type\":3,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads3=payload+i+end3
    
    end4="\",\"type\":4,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads4=payload+i+end4
    
    end5="\",\"type\":5,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads5=payload+i+end5
    
    end6="\",\"type\":5,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads6=payload+i+end6
    time.sleep(3)
    response1 = requests.request("POST", url, headers=headers, data=payloads1)
    print(response1.text) 
    time.sleep(3)
    response2 = requests.request("POST", url, headers=headers, data=payloads2) 
    print(response2.text) 
    time.sleep(3)
    response3 = requests.request("POST", url, headers=headers, data=payloads3)
    print(response3.text) 
    time.sleep(3)
    response4 = requests.request("POST", url, headers=headers, data=payloads4)
    print(response4.text) 
    time.sleep(3)
    response5 = requests.request("POST", url, headers=headers, data=payloads5)
    print(response5.text) 
    time.sleep(3)
    response6 = requests.request("POST", url, headers=headers, data=payloads6)
    print(response6.text) 
    #print(response.request.headers)
    #print(response.request.body)
       
    nums=nums+1
    print(nums)
print("刷分结束")