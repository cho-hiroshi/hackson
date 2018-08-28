# coding: utf-8
import requests
import re


class Solr(object):
    def __init__(self, address):
        self.address = address

    def retrive(self, query):
        url = 'http://{}/solr/hackson/select'.format(self.address)
        params = {'q': 'section:*^100%20OR%20sentence:*^10'}
        response = requests.get(url, params=params)
        if not response.status_code == '200':
            raise Exception()
        result = response.json()
        retreive_result = []
        for sentence in result['response']['docs']:
            l = self._split_sentence(query, sentence['sentence'])
            retreive_result.extend(l)
        return retreive_result

    def _split_sentence(self, query, sentence):
        result_list = []
        match_iter = re.finditer(query, sentence)
        for match in match_iter:
            triple = {}
            triple['pre'] = sentence[: match.start()]
            triple['query'] = sentence[match.start(): match.end()]
            triple['suf'] = sentence[match.end:]
            result_list.append(triple)
        return result_list

    def mock_retrive(self, query):
        t1 = {'pre': 'pre1', 'query': 'query1', 'suf': 'suf1'}
        t2 = {'pre': 'pre2', 'query': 'query2', 'suf': 'suf3'}
        t3 = {'pre': 'pre3', 'query': 'query2', 'suf': 'suf3'}
        return [t1, t2, t3]

