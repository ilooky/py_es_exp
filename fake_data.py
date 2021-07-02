from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://localhost:9200/")

jia = {
    "continent": "",
    "task_name": "网信办探测任务一",
    "urgency_manage": "",
    "os_family": "",
    "isp": "",
    "service_info": '[{"protocol":"tcp","port":80,"service":"http","out_net_distinguish":1,"server_url":"",'
                    '"version":""}]',
    "device_num": 1,
    "protocol_list": "23,80",
    "insert_time": 1606030611000,
    "device_type": "厂商系列",
    "industry": "",
    "task_id": "36",
    "source": "0",
    "is_ipv6": False,
    "server_domain": "",
    "institution_name": "",
    "enabled": "1",
    "mac": "",
    "institution_id": "0",
    "asset_falg": "0",
    "manufacturer": "杭州华三通信技术有限公司",
    "update_time": 1606030611000,
    "asset_name": "Web user login",
    "asset_worth": "",
    "asset_manage": "",
    "asset_type": "1,2",
    "model": "",
    "brand": "H3C",
    "ip": "192.16.127.12",
    "history_state": "0",
    "alive_state": "1",
    "protect_grade": "",
    "os": "",
    "port_list": "23,80",
    "port_num": 2,
    "service_num": 1,
    "banner": "****************************************************************************** * Copyright (c) "
              "2004-2011 Hangzhou H3C Tech. Co., Ltd. All rights reserved. * * Without the owner's prior written "
              "consent, * * no decompiling or reverse-engineering shall be allowed. * "
              "****************************************************************************** Login authentication "
              "Username:",
    "country_code": "",
    "device_info": '[{"protocol":"tcp","port":23,"service":"telnet","out_net_distinguish":1,"type":"厂商系列",'
                   '"version":""}]',
    "application_num": 0,
    "application_info": "",
    "asn": "",
    "gateway": ""
}


def save():
    for i in range(9):
        jia['ip'] = i
        es.index(index='asset_discovery', doc_type='doc', body=jia)


query_json = {
    "query": {
        "match_all": {

        }
    }
}


def query():
    print(es.search(index='asset_discovery', filter_path=['hits.total', 'hits.hits._source'], body=query_json))
    # print(es.search(index='asset_discovery', body=query_json))


if __name__ == '__main__':
    for i in range(1000):
        save()
    query()
