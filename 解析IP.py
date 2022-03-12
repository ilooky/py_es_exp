import requests

ip_list = [
    "113.31.115.247",
    "113.31.115.247",
]

url = "http://api01.aliyun.venuscn.com/ip"

headers = {"Authorization": "APPCODE " + "179b14f95a9a47c4b3d1232189fd60b5"}


def get_ip():
    return ip_list


def parse(ip_txt):
    res = requests.get(url=url, params={"ip": ip_txt}, headers=headers)
    if res.status_code == 200:
        return res.json()['data']
    else:
        print("net error:" + res.status_code.__str__())


if __name__ == '__main__':
    ips = get_ip()
    for ip in ips:
        data = parse(ip)
        # print(data)
        print(data['ip'], data['isp'], data['city'], data['city_id'])
