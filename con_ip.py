#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.orm import declarative_base, session, sessionmaker

# mysql+mysqlconnector://户名: 密码@IP地址:端口号/数据库名称
engine = create_engine("mysql+mysqlconnector://root:1234rewq!@192.168.1.8:3306/dev_us_auto")
Base = declarative_base()


class Information(Base):
    __tablename__ = "hb_unit_information_1"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip_range = Column(String)
    county = Column(String)

    def __init__(self, name, ip_range, county):
        self.name = name
        self.ip_range = ip_range
        self.county = county


class Information2(Base):
    __tablename__ = "hb_unit_information_2"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip_range = Column(String)
    county = Column(String)

    def __init__(self, name, ip_range, county):
        self.name = name
        self.ip_range = ip_range
        self.county = county


DBSession = sessionmaker(bind=engine)
db_session = DBSession()
result = db_session.query(Information).all()

merge = {}
county_dict = {}
for row in result:
    if not row.ip_range:
        continue
    ip_str = row.ip_range.replace(" ", ",") \
        .replace(" 到", ",") \
        .replace("  ", ",") \
        .replace("、", ",") \
        .replace("，", ",") \
        .replace(",,", ",")
    # print(ip)
    if not ip_str:
        continue
    county_dict[row.name] = row.county
    if merge.get(row.name) is None:
        merge[row.name] = ip_str
    else:
        if ip_str.find(",") == -1:
            merge[row.name] = merge[row.name] + "," + ip_str
        else:
            new_ip_list = filter(lambda x: merge[row.name].find(x) == -1, ip_str.split(","))
            if len(list(new_ip_list)) != 0:
                merge[row.name] = merge[row.name] + "," + ",".join(list(new_ip_list))

for k in merge:
    db_session.add(Information2(k, merge[k], county_dict[k]))
db_session.flush()
db_session.commit()
