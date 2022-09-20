# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 06:47:49 2021

@author: Administrator
"""

ids=["1375058374525325312", "1375028008691306496", "1375027859214700544", "1375027689479606272", "1375027477751140352", "1375026948530638848", "1375005007249805312", "1375004851301388288", "1375004641934315520", "1375004545859588096", "1375004411654443008", "1374997577681997824", "1374972703030775808", "1374972336272445440", "1374972074120056832", "1374971733727121408", "1374971526239096832", "1374971399852134400", "1374896190734340096", "1374876251520634880", "1374876040937213952", "1374875855381204992", "1374673708706304000", "1374673493312016384", "1374673207730245632", "1374673058303971328", "1374659161761124352", "1374659071566811136", "1374658939202965504", "1374658757845454848", "1374658570141962240", "1374658112908300288", "1374635091497717760", "1374607349632864256", "1374603881941700608", "1374603746373406720", "1374553639913394176", "1374553482270478336", "1374519321694441472", "1374519074624770048", "1374515586662535168", "1374515284668452864", "1374336328157761536", ]
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
'Cookie':'token=token=35d0327a-b5f0-4a26-94bb-18aec8a546e1'
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