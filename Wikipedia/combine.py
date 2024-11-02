import requests

def get_wikipedia_full_text(page_title, user_agent):
    # 组建API请求的URL
    url = "https://zh.wikipedia.org/w/api.php"

    headers = {
        'User-Agent': user_agent
    }

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,  # 获取纯文本内容（不含HTML标签）
        "titles": page_title,
        "converttitles": True,  # 自动转换为简体中文
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # 确保请求成功

    # 解析响应
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))  # 获取第一个页面对象

    # 返回页面的全文
    return page.get("extract", "")

# 设置一个简体中文Chrome环境的用户代理
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"

# 指定的文章标题
titles = [
    "俄罗斯入侵乌克兰中的中华人民共和国",
    "俄乌战争",
    "2022年至今的俄乌和平谈判",
    "俄罗斯入侵乌克兰",
    "2021年—2023年俄乌危机的虚假信息"
]

# 获取每篇文章的全文
full_texts = [get_wikipedia_full_text(title, user_agent) for title in titles]
