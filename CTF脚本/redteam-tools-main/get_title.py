# -*- coding:utf-8 -*-
# 棱角团队 by shihuang
# python3
import requests
from bs4 import BeautifulSoup
from threading import Thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed
import time,random
requests.packages.urllib3.disable_warnings()


def get_http_banner(url):
    try:
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        ]
        r = s.get('http://' + url,
                  headers={'UserAgent': random.choice(user_agent_list), 'Accept-Language': 'zh-CN,zh;q=0.9'}, timeout=1,
                  verify=False, allow_redirects=True)
        if r.status_code == 400:
            r = s.get('https://' + url,
                      headers={'UserAgent': random.choice(user_agent_list), 'Accept-Language': 'zh-CN,zh;q=0.9'},
                      timeout=1, verify=False,
                      allow_redirects=True)
            encoding = r.encoding
            soup = BeautifulSoup(r.text.encode(encoding).decode('utf-8'), 'html.parser')
            if soup.title == None:
                #args = ('https://' + url, "Title could not be found!", r.status_code, ip_port[0], ip_port[1])
                #self.q.put(args)
                return ["Title could not be found!", r.status_code, 'https://' + url,url]
            else:
                #args = ('https://' + url, soup.title.text.strip('\n').strip(), r.status_code, ip_port[0], ip_port[1])
                #self.q.put(args)
                return [soup.title.text.strip('\n').strip(), r.status_code, 'https://' + url,url]
        else:
            encoding = r.encoding
            soup = BeautifulSoup(r.text.encode(encoding).decode('utf-8'), 'html.parser')
            if soup.title == None:
                #args = ('http://' + url, "Title could not be found!", r.status_code, ip_port[0], ip_port[1])
                #self.q.put(args)
                return ["Title could not be found!", r.status_code, 'http://' + url,url]
            else:
                #args = ('http://' + url, soup.title.text.strip('\n').strip(), r.status_code, ip_port[0], ip_port[1])
                #self.q.put(args)
                return [soup.title.text.strip('\n').strip(), r.status_code, 'http://' + url,url]
    except Exception as ex:
        print(ex)
        pass


def out(msg):
    msg='"'+'","'.join(msg)+'"'
    with open('out.csv', 'a',encoding='utf-8-sig') as f:
        f.write(msg + '\n')

def main():
    f = open('url.txt','r')
    out(["url", "title", "state_code"])
    with ThreadPoolExecutor(max_workers=100) as t:
        obj_list = []
        for url in f.readlines():
            url = url.strip('\n')
            #print(url)
            obj = t.submit(get_http_banner, url)
            obj_list.append(obj)

        for future in as_completed(obj_list):
            data = future.result()
            #print(type(data))
            if isinstance(data,list):
                print(data)
                args = [str(data[2]),str(data[0]),str(data[1])]
                out(args)




if __name__ == "__main__":
    start = time.time()
    main()
    print('[info]耗时：%s' % (time.time() - start))

