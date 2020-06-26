# -*- coding: utf-8 -*-

import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
    BeautifulSoup.find_all = BeautifulSoup.findAll


class mdbg(object):
    @classmethod
    def _get_response(cls, word, simplified=0):
        res = requests.get(
            url="https://www.mdbg.net/chinese/dictionary?page=worddict",
            params={
                "wdrst": 0,
                "wdqb": word.lower().encode("utf-8")
            },
            headers={
                'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'
            }
        )
        return res.content.decode("utf-8")

    @classmethod
    def _parse_response(cls, response_body):
        soup = BeautifulSoup(response_body, "html.parser")
        table_body = soup.find('table', {'class': 'wordresults'})
        if table_body:
            rows = table_body.findAll('tr', {'class': 'row'})
            results = [
                {
                    'hanzi': row.find('div', {'class': 'hanzi'}).text,
                    'pinyin': row.find('div', {'class': 'pinyin'}).text,
                    'defs': row.find('div', {'class': 'defs'}).text
                }
                for row in rows
            ]
        else:
            results = []
        return results
