from scrap import Scraper
from pymongo import MongoClient
from tqdm import tqdm

#change for your mongodb credentials
MONGO_CONNECTION = ''
MONGO_PORT = 27017
MONGO_USER = ''
MONGO_PASSWORD = ''
MONGO_DB = 'test'

connection = MongoClient(MONGO_CONNECTION,MONGO_PORT)
database = connection[MONGO_DB]

scrap = Scraper()
scrap.get_links(1)

for link in tqdm(scrap.links):
    url = scrap.base_url + link

    if database.col.find_one({'Url':url}) == None:
        article = scrap.scrap_article(link)
        database.col.insert_one(article)
        
    