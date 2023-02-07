import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from airflow.models import Variable
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

def scrape_random_memes():
    print('Scraping random memes')
    url = 'https://www.generatormix.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    page = requests.get(url + '/random-memes', headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    memes = []

    memes_elements = soup.find_all('div', class_='col-4')

    for meme_element in memes_elements:
        print(meme_element)
        meme = {}
        meme['title'] = meme_element.find('h3').text
        src = meme_element.find('img')['data-src']
        img = url + src
        meme['img'] = img
        memes.append(meme)

    print(memes)

with DAG(
    dag_id='twitter_scrapper',
    start_date=days_ago(2),
    schedule_interval=None,
    catchup=False,
) as dag:
    scrape_random_memes = PythonOperator(
        task_id='scrape_random_memes',
        python_callable=scrape_random_memes
    )

