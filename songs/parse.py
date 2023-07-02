from bs4 import BeautifulSoup
import requests
import psycopg2

def parse_and_store:
    url = ''
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
