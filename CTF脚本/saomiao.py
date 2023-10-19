import requests

url1 = 'http://challenge-27ed27686e37809f.sandbox.ctfhub.com:10800/'		# url为被扫描地址，后不加‘/’

# 常见的网站源码备份文件名
list1 = ['web', 'website', 'backup', 'back', 'www', 'wwwroot', 'temp']
# 常见的网站源码备份文件后缀
list2 = ['tar', 'tar.gz', 'zip', 'rar','bak']

for i in list1:
    for j in list2:
        back = str(i) + '.' + str(j)
        url = str(url1) + '/' + back
        print(back + '    ', end='')
        print(requests.get(url).status_code)