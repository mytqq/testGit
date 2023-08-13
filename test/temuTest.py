import requests

url = "https://www.temu.com/api/poppy/v1/goods_detail?scene=goods_detail_bought_together"
payload = {
    "scene": "goods_detail_bought_together",
    "goodsId": 601099512518740,
    "goodsSkuPairs": [
        {
            "goodsId": 601099512518740,
            "skuId": 17592191149498,
            "count": 1,
            "selected": True
        }
    ],
    "listId": "256ct5_bought_together",
    "mainGoodsIds": ["601099512518740"],
    "offset": 7,
    "pageListId": "goods_detail_page_h0l8ub",
    "pageSize": 10,
    "pageSn": 10032,
    "skuId": 17592191149498
}

headers = {
    "Content-Type": "application/json",
    "Referer": "https://www.temu.com",
    "Origin": "https://www.temu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.json())
