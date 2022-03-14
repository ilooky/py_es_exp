import json

import requests

url = "https://restapi.amap.com/v3/config/district?parameters1"
key = "8e2905df4e2e39eac87ff3ac39a3f83e"
txt_source_path = "./ip.txt"
txt_dest_path = "./ip_tidy.txt"


def get_ip():
    lines = []
    with open(txt_source_path, encoding='utf-8', mode='r') as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines


def parse(address):
    res = requests.get(url=url, params={"keywords": address, "key": key, "subdistrict": "0", "offset": "1"})
    if res.status_code == 200:
        return json.loads(res.text).get("districts")[0]
    else:
        print("net error:" + res.status_code.__str__())


if __name__ == '__main__':
    ips = get_ip()
    fo = open(txt_dest_path, "a", encoding='utf-8')
    print("地址     行政编号     经度,纬度")
    fo.write("地址     行政编号     经度,纬度")
    for ip in ips:
        data = parse(ip)
        result = data['name'] + "    " + data['adcode'] + "     " + data['center']
        fo.write("\n" + result)
        print(result)
