import requests
import json

def ask_gpt(question):
    url = "https://api.binjie.fun/api/generateStream"
    headers = {
        "Host": "api.binjie.fun",
        "Content-Length": "136",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://chat18.aichatos.xyz",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://chat18.aichatos.xyz/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Priority": "u=1, i"
    }
    data = {
        "prompt": question,
        "userId": "#/chat/1720928513671",
        "network": True,
        "system": "",
        "withoutContext": False,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_content = response.content.decode('utf-8')
        print("Response data:", response_content)
        return response_content
    else:
        print("Failed to get data. Status code:", response.status_code)