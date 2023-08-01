import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, save_dir):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    if response.status_code != 200:
        print("无法访问网站")
        return

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 获取所有图片标签
    img_tags = soup.find_all("img")

    # 遍历图片标签，下载图片
    for img in img_tags:
        img_url = img.get("src")
        if img_url:
            img_url = urljoin(url, img_url)
            try:
                # 发送HTTP请求下载图片
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    # 构造保存路径
                    img_name = os.path.basename(img_url)
                    save_path = os.path.join(save_dir, img_name)

                    # 保存图片到本地
                    with open(save_path, "wb") as f:
                        f.write(img_response.content)
                    print(f"下载图片：{img_url}")
                else:
                    print(f"无法下载图片：{img_url}")
            except requests.RequestException:
                print(f"无法访问图片链接：{img_url}")
        else:
            print("找不到图片链接")

if __name__ == "__main__":
    # 要爬取的网站URL
    target_url = "https://mbsifu.com/"
    # 保存图片的目录
    save_directory = "下载存放地址"

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    download_images(target_url, save_directory)
