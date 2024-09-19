
import requests
import re
BV=input('请输入您要查询的Bv号')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}  #模拟成火狐浏览器
response = requests.get(f"https://www.bilibili.com/video/{BV}",headers=headers)  #模拟请求url
response.encoding='utf-8'
pattern= r'http://i\d\.hdslb\.com/bfs/archive/(.*)(\.png|\.jpg|\.webp)'# 使用正则表达式查找所有匹配的图片链接
matches=re.findall(pattern,response.text)
for match in matches:
    full_link = f"http://i0.hdslb.com/bfs/archive/{match[0]}{match[1]}"#将匹配到的文本组成链接
    print(full_link)