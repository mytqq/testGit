# 一个优秀的 Python 软件包管理工具 pipenv控制台输入。  pip install pipenv   安装后，请执行：  pipenv install

import requests
import  json
from bs4 import BeautifulSoup

from flask import Flask, request

app = Flask(__name__)

# （1）Requests：一个Python第三方库，可以处理HTTP请求和响应。
# （2）BeautifulSoup：一个Python的HTML/XML解析器库，可以快速解析页面中的元素。
# （3）Scrapy：一个Python爬虫框架，具有高效、快速的爬取速度、数据处理和管理等特点。
# （4）Selenium：一个自动化测试工具，可以模拟用户操作浏览器来访问网站并获取所需数据。


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
    # 'Referer':'https://www.aliprice.com/Index/searchbyimage.html?ADID=18&image=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F51sQ-GDgWGL._AC_UL160_SR160%2C160_.jpg&plat=1688_lite&phash=LFA2QgMuLoRyWbR3shAEM9xqmM6sW746kv0m2XHv%2BAryLxtij2U9O1uVrLZyli5AvXqb8bhXRZsJF%2Fm40i9%2BBw%3D%3D&cateid2=3&uploadkey=1689845721-816.jpeg'
    
}


# 替换字符串中的符号
def replace_symbol(str):
    str = str.replace(':', '%3A')
    str = str.replace('/', '%2F')
    str = str.replace('?', '%3F')
    str = str.replace('&', '%26')
    str = str.replace('=', '%3D')
    str = str.replace('+', '%2B')
    # str = str.replace('%20', '+')
    # str = str.replace('%27', '%22')
    # str = str.replace('%28', '%28')
    # str = str.replace('%29', '%29')
    # str = str.replace('%21', '%21')
    # str = str.replace('%24', '%24')
    # str = str.replace('%2C', '%2C')
    # str = str.replace('%26', '%26')
    return str

def getUrl(url):
    response = requests.get(url,headers=headers);
    response.encoding = "utf-8-sig"
    return response


@app.route('/geturl', methods=['GET'])
def handle_request():
    # 获取前端发送的查询参数
    # url = request.args.get('url')
    url = replace_symbol(request.args.get('url'))


if __name__ == '__main__':
    app.run()


str="https://images-na.ssl-images-amazon.com/images/I/61KDpa+vM6L._AC_UL160_SR160,160_.jpg"
# 运行replace_symbol方法

print(replace_symbol(str))


urlO = "https://www.aliprice.com/Index/searchbyimage.html?ADID=100&image="+replace_symbol(str)+"&cateid2=0&cateid4=&plat=1688_lite&modal=1"
ress=getUrl(urlO).json()
print(ress["phash"])

url2 = "https://www.aliprice.com/Index/searchbyimage.html?ADID=100&image="+str+"&cateid2=0&cateid4=&plat=1688_lite&modal=2&uploadkey="+ress["uploadkey"]+"&phash="+ress["phash"]
print()
print(url2)

# print(getUrl(url2).json()["html"])


# 定位html的元素
soup = BeautifulSoup(getUrl(url2).json()["html"], 'html.parser')
# find定位img元素 并get提取src属性值
img_tag_1 = soup.find_all('img')[0].get('src')
print(img_tag_1)
img_tag_2 = soup.find_all('img')[1].get('src')
print(img_tag_2)

data = {
    "img_tag_1": img_tag_1,
    "img_tag_2": img_tag_2
}
print(data)
print(json.dumps(data))



# urlO = "https://www.aliprice.com/Index/searchbyimage.html?ADID=100&image="+str+"&cateid2=0&cateid4=&plat=1688_lite&modal=1"
# response = requests.get(urlO,headers=headers);
# response.encoding = "utf-8-sig"
# print(response.text)
# resultText=response.json()["phash"]
# print("1111resultText："+resultText)



# url2 = "https://www.aliprice.com/Index/searchbyimage.html?ADID=100&image="+str+"&cateid2=0&cateid4=&plat=1688_lite&modal=2&uploadkey="+response.json()["uploadkey"]+"&phash="+response.json()["phash"]+""
# print(url2)
# response2 = requests.get(url2,headers=headers);
# resultText2=response2.text
# if len(resultText2) <= 1 :
#     print("返回为空");
#     print(len(resultText2));
#     exit
# else:
#     print("数据结果："+resultText2)

