import datetime
from airflow.models import Variable
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

def scrape_random_memes():
    print('Scraping random memes')


with DAG(
    dag_id='twitter_scrapper',
    start_date=days_ago(2),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    scrape_tweets = PythonOperator(
        task_id='scrape_tweets',
        python_callable=scrape_random_memes
    )

