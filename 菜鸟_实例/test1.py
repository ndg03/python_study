# 所在包    python
# 项目名称  test1
# 日期     2023/4/8/ 23:16
# 作者     你大锅
import requests
import json

# 设置查询参数
appid = 730
num_items_per_page = 5000
start_item = 0

# 使用Steam市场API进行查询
while True:
    url = f"https://steamapis.com/steam-market-api/items/{appid}/{num_items_per_page}/{start_item}"
    response = requests.get(url)

    # 解析JSON数据并获取饰品图片URL
    data = json.loads(response.content)
    for item in data["items"]:
        image_url = item["image"]

        # 下载高清图片并保存到本地
        response = requests.get(image_url)
        item_name = item["name"].replace("/", "-")
        with open(f"{item_name}.png", "wb") as f:
            f.write(response.content)

    # 检查是否还有更多的饰品需要下载
    if data["total_count"] <= start_item + num_items_per_page:
        break
    start_item += num_items_per_page
