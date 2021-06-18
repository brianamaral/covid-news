from scrap import Scraper
from sqlalchemy import create_engine
import pandas as pd
from tqdm import tqdm
from schedule import every, repeat, run_pending
import time

#change for your POSTGRES credentials
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
POSTGRES_ADDRES = ''
POSTGRES_DATABASE = ''

engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(POSTGRES_USER,POSTGRES_PASSWORD,
                                                                  POSTGRES_ADDRES,POSTGRES_DATABASE))
connection = engine.connect()

scrap = Scraper()
scrap.get_links(1)

df_articles = pd.DataFrame(columns=['title','date','text','url','author'])

@repeat(every(30).seconds,scrap,df_articles)
def scraped_page_to_postgres(scrap,df_articles):
    for link in tqdm(scrap.links):
        url = scrap.base_url + link

        article = scrap.scrap_article(link)

        article_row = {'title':article['Titulo'],'date':article['Data'],
                   'text':article['Texto'],'url':article['Url'],
                   'author':article['Autor']}
        df_articles = df_articles.append(article_row,ignore_index=True)

    df_articles.to_sql('articles',connection,if_exists='append',index=False)       

while True:
    run_pending()
    time.sleep(1)