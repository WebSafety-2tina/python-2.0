这道题的脚本如下，还可以继续优化
#经常出现执行了但是不弹flag的情况，多试几次就行了
from bs4 import BeautifulSoup
import requests

r = requests.Session()
s = r.get(http123.206.87.2408002qiumingshan)
s.encoding = 'utf-8'
text = s.text
soup = BeautifulSoup(text)
tag = soup.div
express = str(tag.string)
express = express[0  -3]
answer = eval(express)
ans = {value  answer}
flag = r.post('http123.206.87.2408002qiumingshan', data = ans)
print(flag.text)