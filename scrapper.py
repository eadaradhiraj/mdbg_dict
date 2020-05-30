import requests
from bs4 import BeautifulSoup as soup

words = []
result = requests.get(
    "https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=super")

# print(result.status_code)

res = result.content

page_soup = soup(res, 'html.parser')

tbody = page_soup.find("tbody")

trs = tbody.find_all("tr")

for tr in trs:
    tds = tr.find_all("td")
    tds = [x.text.strip() for x in tds]
    # hanzi_word = pinyin.text.strip()
    # print(cols)
    if(len(tds) > 1):
        words.append(
            {"hanzi": tds[1], "pinyin": tds[0].encode('ascii', 'ignore').decode("utf-8", "ignore"), "definition": tds[2]})

# print(words)

import pandas

df = pandas.DataFrame(data=words)
df.to_csv("words.csv", sep=',', index=False)
# print(len(all_titles))
