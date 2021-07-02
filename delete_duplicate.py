#!/usr/local/bin/python3

from elasticsearch import Elasticsearch, helpers

ES_HOST = 'localhost:9200'
ES_INDEX = 'asset_discovery'
DUPLICATE_KEY = 'ip'
COUNT = 5000

es = Elasticsearch(ES_HOST)
dict_of_duplicate_docs = {}


def populate_dict_of_duplicate_docs(hit):
    _id = hit["_id"]
    if hit['_source'].get(DUPLICATE_KEY):
        combined_key = str(hit['_source'][DUPLICATE_KEY])
        dict_of_duplicate_docs.setdefault(combined_key, []).append(_id)
    else:
        dict_of_duplicate_docs.setdefault("None_IP", []).append(_id)


def scroll_over_all_docs():
    count = 0
    result = helpers.scan(es, index=ES_INDEX)
    for hit in result:
        populate_dict_of_duplicate_docs(hit)
        count += 1
        if count == COUNT:
            break


def loop_over_hashes_and_remove_duplicates():
    items = dict_of_duplicate_docs.items()
    for ip, array_of_ids in items:
        dup_ids = len(array_of_ids)
        print("ip: ", ip, "count: ", dup_ids)
        if dup_ids > 1:
            for i in range(dup_ids):
                if i == 0:
                    continue
                es.delete(index=ES_INDEX, doc_type='doc', id=array_of_ids[i])


if __name__ == '__main__':
    scroll_over_all_docs()
    loop_over_hashes_and_remove_duplicates()
