# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 06:47:49 2021

@author: Administrator
"""

ids=["1321730705843163136", "1321703127400976384"]

import random
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
'Cookie':'token=c0e041ae-d941-4d8f-b919-226e034f0a48'
}


def timesleep():
     i=random.randint(15,50)
     print(i)
     time.sleep(i)


payload="{\"isLoadTip\":\"...\",\"user_id\":\"1316927879329746944\",\"wechat_share_task_id\":\""
#for i in range(173740533760,973740533760):
num1=1
num2=1
num3=1
num4=1
num5=1
num6=1

for i in ids:
    #id="1414915"+str(i)    
    end1="\",\"type\":1,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads1=payload+i+end1   
    timesleep()
    response1 = requests.request("POST", url, headers=headers, data=payloads1)
    print(response1.text)    
    print(i)
    num1=num1+1
    print(num1)
    
for i in ids:       
    end2="\",\"type\":2,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads2=payload+i+end2   
    timesleep()
    response2 = requests.request("POST", url, headers=headers, data=payloads2) 
    print(response2.text)    
    print(i)
    num2=num2+1
    print(num2)    
    
    
    
for i in ids:
    end3="\",\"type\":3,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads3=payload+i+end3
  
    timesleep()
    response3 = requests.request("POST", url, headers=headers, data=payloads3)
    print(response3.text) 
   
    print(i)
    num3=num3+1
    print(num3)    
    
      
    
    
for i in ids:        
    end4="\",\"type\":4,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads4=payload+i+end4    
   
    timesleep()
    response4 = requests.request("POST", url, headers=headers, data=payloads4)
    print(response4.text) 
    
    print(i)
    num4=num4+1
    print(num4)    
    
for i in ids:
    end5="\",\"type\":5,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads5=payload+i+end5    
    timesleep()
    response5 = requests.request("POST", url, headers=headers, data=payloads5)
    print(response5.text)    
    print(i)
    num5=num5+1
    print(num5)    
    
for i in ids:
    end6="\",\"type\":5,\"token_header\":\"xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D\"}"
    payloads6=payload+i+end6
   
    timesleep()
    response6 = requests.request("POST", url, headers=headers, data=payloads6)
    print(response6.text) 
    #print(response.request.headers)
    #print(response.request.body)
    print(i)
    num6=num6+1
    print(num6)    
 
    
print("刷分结束")
