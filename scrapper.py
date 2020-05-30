from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import csv
all_titles = []

# filename = "titles.csv"
# f = open(filename, 'w')
# headers = "titles"
# f.write(headers)
for i in range(1,161):
    # my_url = ''
    my_url = "https://www.newegg.com/global/in-en/p/pl?d=graphics&page="+str(i)

    client = ureq(my_url)

    raw_html = client.read()

    page_soup = soup(raw_html, 'html.parser')

    titles = page_soup.findAll("div", {"class": "item-title"})

    # print(page_soup.findAll("div", {"class": "item-title"}))
    for title in titles:
        ttl = title.a.text
        all_titles.append(ttl.strip())
        # f.write(ttl.strip())

# with open("titles.csv", 'w', newline='') as myfile:
#      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#      wr.writerow(all_titles)

import pandas

df = pandas.DataFrame(data={"titles": all_titles})
df.to_csv("titles.csv", sep=',',index=False)
print(len(all_titles))

