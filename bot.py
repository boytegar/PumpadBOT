import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime

headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'referer': 'https://tg.pumpad.io/lottery/',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
    }

def load_credentials():

    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        return queries
    except FileNotFoundError:
        print("File query_id.txt tidak ditemukan.")
        return [  ]
    except Exception as e:
        print("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]

def getuseragent(index):
    try:
        with open('useragent.txt', 'r') as f:
            useragent = [line.strip() for line in f.readlines()]
        if index < len(useragent):
            return useragent[index]
        else:
            return "Index out of range"
    except FileNotFoundError:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except Exception as e:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'

def getassets(query):
    url = 'https://tg.pumpad.io/referral/api/v1/lottery/assets'
    headers['Authorization'] = f"tma {query}"

    response = requests.get(url, headers=headers)
    try:
        
        if response.status_code >= 500:
            print(response.text)
            return None
        elif response.status_code >= 400:
            print(response.text)
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getmission(query):
    url = 'https://tg.pumpad.io/referral/api/v1/tg/missions'
    headers['Authorization'] = f"tma {query}" 
    response = requests.get(url, headers=headers)  
    try:
        
        if response.status_code >= 500:
            print(response.text)
            return None
        elif response.status_code >= 400:
            print(response.text)
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def clearmission(query, id):
    url =f'https://tg.pumpad.io/referral/api/v1/tg/missions/check/{id}'
    payload = {}
    headers['Authorization'] = f"tma {query}"
    response = requests.post(url, headers=headers, json=payload)
    try:
        if response.status_code >= 500:
            print(response.text)
            return None
        elif response.status_code >= 400:
            print(response.text)
            return None
        elif response.status_code >= 200:
            return "done"
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getlottery(query):
    url = 'https://tg.pumpad.io/referral/api/v1/lottery'
    headers['Authorization'] = f"tma {query}"

    response = requests.get(url, headers=headers)
    try:
        
        if response.status_code >= 500:
            print(response.text)
            return None
        elif response.status_code >= 400:
            print(response.text)
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def postlottery(query):
    url = 'https://tg.pumpad.io/referral/api/v1/lottery'
    headers['Authorization'] = f"tma {query}"

    response = requests.post(url, headers=headers)
    try:
        
        if response.status_code >= 500:
            print(response.text)
            return None
        elif response.status_code >= 400:
            print(response.text)
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {round(sec)} seconds")


def main():
    print(r"""
              
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sansxgroup
              
          """)
    while True:
        delay_time = random.randint(32000, 32000)
        queries = load_credentials()
        for index, query in enumerate(queries):
            start_time = time.time()
            headers['User-Agent'] = getuseragent(index)
            print()
            print(f"========== Account {index+1} ==========")
            data_assets = getassets(query)
            if data_assets is not None:
                assets = data_assets.get('assets')
                if len(assets) == 0:
                    print("no have assets")
                else:
                    for ass in assets:
                        amount = int(ass.get('amount'))
                        token = ass.get('token')
                        decimals = token.get('decimals')
                        pows = pow(10, decimals)
                        print(f"Token Name : {token.get('name', 'Star')} | Amount : {float(amount/pows)}")
            else:
                print("Error get data")
            time.sleep(3)
            print()
            print("get list task")
            data_mission = getmission(query)
            if data_mission is not None:
                mission_list = data_mission.get('mission_list')
                for mission in mission_list:
                    done = mission.get('done_time')
                    detail_mission = mission.get('mission')
                    id = detail_mission.get('id')
                    name = detail_mission.get('name')
                    if done == 0:
                        if id not in [2,6]:
                            data_done_mission = clearmission(query, id)
                            if data_done_mission == 'done':
                                print(f"Task : {name} is Done")
                            time.sleep(3)

            print()
            print('get data lottery')
            time.sleep(3)
            lottery = postlottery(query)
            if lottery is not None:
                reward = lottery.get('reward')
                print(f"Draw 1 Reward : {reward.get('name')}")
                time.sleep(5)
            time.sleep(1)
            data_lottery = getlottery(query)
            if data_lottery is not None:
                draw_count = data_lottery.get('draw_count')
                time.sleep(1)
                for i in range(draw_count):
                    lottery = postlottery(query)
                    if lottery is not None:
                        reward = lottery.get('reward')
                        print(f"Draw {i+2} Reward : {reward.get('name')}")
                        time.sleep(5)
        end_time = time.time()
        delay = delay_time - (end_time-start_time)
        printdelay(delay)
        time.sleep(delay)

if __name__ == "__main__":
    main()