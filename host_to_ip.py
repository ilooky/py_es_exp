#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import gethostbyname

DOMAIN = "./host.txt"

with open(DOMAIN, encoding='utf-8', mode='r') as f:
    for line in f.readlines():
        try:
            host = gethostbyname(line.strip('\n'))
        except Exception as e:
            with open('no_ip_error.txt', 'a+') as ERR:  # error.txt为没有IP绑定的域名
                ERR.write(line.strip() + '\n')
        else:
            with open('host_to_ip_result.txt', 'a+') as r:
                r.write(line.strip('\n') + '                  ')
                print(line, host)
                r.write(host + '\n')
