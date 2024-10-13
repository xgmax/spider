import ddddocr as ddddocr
import requests
from bs4 import BeautifulSoup

s=requests.Session()
#伪装头信息
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
}
#伪装ip
proxies = {
    'http':'127.0.0.1:7890',
    'https':'127.0.0.1:7890'
}
#请求登录信息
login = s.get('https://www.nowapi.com/?app=account.login',headers=headers,proxies=proxies)

for item in s.cookies.itervalues():
    print(item[0],":",item[1])

#使用bs4解析页面获取验证码的地址
sout = BeautifulSoup(login.text,'html.parser')
image_url = sout.find_all(id='authCodeImg')[0]['src']

#把url识别为图片
requests = s.get(image_url)
if requests.status_code == 200:
    with open("lm.jpg",'wb')as file:
        file.write(requests.content)
else:
    print("下载失败：{requests.status_code}")

#识别图片
ocr=ddddocr.DdddOcr()
image = open("lm.jpg","rb").read()
result = ocr.classification(image)
print(result)
#传递表单数据
data = {
    'usernm':'syl9617016',
    'passwd':'syl123321',
    'authcode':'result',
    'app':'accountr_aja_login'
}
r=s.post('https://www.nowapi.com/index.php?ajax=1',headers=headers,proxies=proxies,data=data)
print(r.text)