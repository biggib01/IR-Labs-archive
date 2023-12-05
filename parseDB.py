from bs4 import BeautifulSoup
from sphinx.util import requests
def parse_db():
    html_doc = requests.get("https://db-engines.com/en/ranking").content
    soup = BeautifulSoup(html_doc, 'html.parser')
    db_table = soup.find("table", {"class": "dbi"})
    all_db = [''.join(s.find('a').findAll(string=True,recursive=False)).strip() for s in
        db_table.findAll("th", {"class": "pad-l"})]
    all_db = list(dict.fromkeys(all_db))
    db_list = all_db[:15]
    db_list = [s.lower() for s in db_list]
    db_list = [[x.strip() for x in s.split()] for s in db_list]
    return db_list