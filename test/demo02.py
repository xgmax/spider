import urllib.request
url = "http://httpbin.org/get"
head = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=head)
proxy_hander = urllib.request.ProxyHandler({"http": "127.0.0.1:7890"})
opener = urllib.request.build_opener(proxy_hander)
response = opener.open(req)
print(response.read().decode())