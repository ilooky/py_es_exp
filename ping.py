from icmplib import ping

host = ping('172.24.186.191', count=2, interval=0.2)
print(host.is_alive)
