
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_historical_draws():
    url = 'https://www.nationallottery.co.za/results/lotto'
    data = []

    for page in range(1, 50):
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        draw_rows = soup.find_all('tr', class_='draw-row')
        for row in draw_rows:
            numbers = [int(td.text) for td in row.find_all('td')[1:7]]
            date = row.find('td')[0].text.strip()
            data.append([date] + numbers)

    df = pd.DataFrame(data, columns=['Date', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6'])
    df.to_csv('data/raw_historical_draws.csv', index=False)

fetch_historical_draws()
