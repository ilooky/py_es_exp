import json

import requests

ip_list = [
    "113.31.115.247",
    "113.31.115.247",
]

# url = "http://api01.aliyun.venuscn.com/ip"
url = "http://ipaddr.market.alicloudapi.com/ip_addr_search/ch/v1"

headers = {"Authorization": "APPCODE " + "179b14f95a9a47c4b3d1232189fd60b5"}


def get_ip():
    DOMAIN = "./ip.txt"
    lines = []
    with open(DOMAIN, encoding='utf-8', mode='r') as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines


def parse(ip_txt):
    # res = requests.get(url=url, params={"ip": ip_txt}, headers=headers)
    res = requests.get(url=url, params={"IP_ADDR": ip_txt}, headers=headers)
    if res.status_code == 200:
        print(res.text)
        return json.loads(res.text).get('IP地址解析实体信息').get('待查询IP地址解析实体信息')
    else:
        print("net error:" + res.status_code.__str__())


if __name__ == '__main__':
    ips = get_ip()
    fo = open("ip_tidy.txt", "a", encoding='utf-8')
    for ip in ips:
        data = parse(ip)
        print(data)
        #     print(data['ip'], data['isp'], data['city'], data['city_id'])
        fo.write("\n" + data['IP地址'] + ":   " + data['省份'] + "," + data['城市'] + "," + data['ISP运营商'] + "," + data[
            '国家行政编码'] + "," + data['GPS'])
