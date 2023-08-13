import requests
from flask import Flask, request
from flask_cors import CORS
import  json
from bs4 import BeautifulSoup
from urllib.parse import unquote
from PIL import Image
import time
import random
import urllib.parse
from threading import Lock

# 在函数外部定义锁对象
lock = Lock()
request_count = 0

# logger = setup_logger('/path/my_logs/amazonError.log')

app = Flask(__name__)
CORS(app)  # 允许所有源访问

# 替换字符串中的符号
def replace_symbol(str):
    str = str.replace(':', '%3A')
    str = str.replace('/', '%2F')
    str = str.replace('?', '%3F')
    str = str.replace('&', '%26')
    str = str.replace('=', '%3D')
    str = str.replace('+', '%2B')
    return str

headers = {
    'referer': 'https://www.aliprice.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'X-Requested-With':'XMLHttpRequest'
}

def getUrl(url):
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8-sig"
    # event.set()  # 设置事件以指示请求完成
    return response

def getUrl(url):
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8-sig"
    return response
    # try:
    #     response = requests.get(url, headers=headers)
    #     response.encoding = "utf-8-sig"
    #     return response
    # except Exception as e:
    #     error_message = f"An error occurred: {str(e)}"
    #     # 调用 log_error 方法来记录错误信息
    #     log_error(logger, error_message)
    #     return None

@app.route('/geturl', methods=['GET'])
def handle_request():

    global request_count
    with lock:
        if request_count >= 30:
            wait_time = random.uniform(2, 3)
            time.sleep(wait_time)
            print(f"到达{request_count}次,随机停止秒：{wait_time}")
            request_count = 0
        request_count += 1

    # 获取前端发送的查询参数
    url = urllib.parse.quote(request.args.get('url'))
    # print("url过滤字符："+url)

    urlO = "https://www.aliprice.com/Index/searchbyimage.html?ADID=100&image="+url+"&cateid2=0&cateid4=&plat=1688_lite&modal=1"
    # print(urlO)
    ress=getUrl(urlO).json()

    url2 = "https://www.aliprice.com/Index/searchbyimage.html?ADID=100&image="+url+"&cateid2=0&cateid4=&plat=1688_lite&modal=2&uploadkey="+ress["uploadkey"]+"&phash="+ress["phash"]
    # print(url2)

    # 使用 BeautifulSoup 解析页面内容
    soup = BeautifulSoup(getUrl(url2).json()["html"], 'html.parser')

    items = soup.find_all("div", class_="item")
    results = []

    for item in items[:4]:
        img = item.find("img")["src"]
        price = item.find(class_="item-price").text
        title = item.find(class_="item-title").text

        a_tag = item.find('a', class_='img-link')  # 使用 item 对象来查找 <a> 标签
        href = a_tag['href']
        extracted_url = href.split('url=')[1].split('&')[0]
        decoded_url = unquote(extracted_url)

        result = {
            "img": img,
            "price": price,
            "title": title,
            "decoded_url": decoded_url
        }
        results.append(result)

    output = {
        "items": results
    }

    return json.dumps(output, ensure_ascii=False)

if __name__ == '__main__':
    app.run()
