import requests
import json


def get_map():
    url = "https://summer-ospp.ac.cn/api/getProList"

    payload = json.dumps({
        "supportLanguage": [],
        "techTag": [
            # "不限",
            # "Java"
        ],
        "programName": "",
        "difficulty": [],
        "pageNum": "1",
        "pageSize": "600",
        "lang": "zh",
        "orgName": []
    })
    headers = {
        'authority': 'summer-ospp.ac.cn',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': '',
        'origin': 'https://summer-ospp.ac.cn',
        'pragma': 'no-cache',
        'referer': 'https://summer-ospp.ac.cn/org/projectlist?lang=zh&pageNum=1&pageSize=50&programName=&techTag=%E4%B8%8D%E9%99%90&techTag=Java',
        'referrer-policy': 'strict-origin-when-cross-origin',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    map_dict = {}
    for row in response.json()['rows']:
        # print(row)
        if row["matchedStudentName"] is None:
            continue
        map_dict[row['programName']] = str(row["proId"])
    # print(len(map_dict))
    return map_dict


if __name__ == "__main__":
    print(get_map())

