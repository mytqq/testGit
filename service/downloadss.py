import requests
from flask import Flask, request
from flask_cors import CORS
import  json
from bs4 import BeautifulSoup
from urllib.parse import unquote

headers = {
    'referer': 'https://www.aliprice.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'X-Requested-With':'XMLHttpRequest'
}

# 替换字符串中的符号
def replace_symbol(str):
    str = str.replace(':', '%3A')
    str = str.replace('/', '%2F')
    str = str.replace('?', '%3F')
    str = str.replace('&', '%26')
    str = str.replace('=', '%3D')
    str = str.replace('+', '%2B')
    return str

def getUrl(url):
    response = requests.get(url,headers=headers);
    response.encoding = "utf-8-sig"
    return response


url = replace_symbol("https://m.media-amazon.com/images/I/712qgWy9k+L._AC_UL320_.jpg")

urlO = "https://www.aliprice.com/Index/searchbyimage.html?ADID=100&image="+url+"&cateid2=0&cateid4=&plat=1688_lite&modal=1"
ress=getUrl(urlO).json()

url2 = "https://www.aliprice.com/Index/searchbyimage.html?ADID=100&image="+url+"&cateid2=0&cateid4=&plat=1688_lite&modal=2&uploadkey="+ress["uploadkey"]+"&phash="+ress["phash"]
print(url2)
print()


# 使用 BeautifulSoup 解析页面内容
soup = BeautifulSoup(getUrl(url2).json()["html"], 'html.parser')

items = soup.find_all("div", class_="item")
results = []

for item in items[:2]:
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

json_data = json.dumps(output, ensure_ascii=False)

# 返回给前端或进行其他操作
print(json_data)