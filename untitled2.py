# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:38:57 2022

@author: Asun
"""

###抽取所有数据历史数据（按时间）重要
import requests
 
url = "https://mt.fjii.com/api/wechatShareTask/list"

#payload="title=&serviceId=1&pageSize=10000&pageNo=1&start_time=2019-07-15%2018%3A35%3A00&end_time=2021-05-31%2018%3A36%3A00&token_header=xOjqTc9vix%2FIQVwVMZmkpCwp4B2WafoeT991Rnx%2FJhmYF6H9Xv46EkHqmsU%2BjVVIZyeIygoJ8sDqdM7d4AfPy19p0ULjujQFFQMUEzFwNVRNw%2FJo8ou6CGPkfB%2B%2FLMlgX2y%2BudFF9SrsZ5kWvffVJg%3D%3D"
payload="serviceId=1&secondaryColumn=1333926968260956160&pageSize=10&pageNo=2"
headers = {
  'Host':'mt.fjii.com'
     
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
