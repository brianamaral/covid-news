from scrap import Scraper
from pymongo import MongoClient
from tqdm import tqdm

# change for your mongodb credentials
MONGO_CONNECTION = ""
MONGO_PORT = 27017
MONGO_USER = ""
MONGO_PASSWORD = ""
MONGO_DB = ""

connection = MongoClient(MONGO_CONNECTION, MONGO_PORT)
database = connection[MONGO_DB]

scrap = Scraper()
scrap.get_all_links()

for link in tqdm(scrap.links):

    article = scrap.scrap_article(link)
    database.col.insert_one(article)
