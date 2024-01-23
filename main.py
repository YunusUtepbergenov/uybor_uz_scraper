from utils.scraper import scrape
from data.variables import sell_url, rent_url

scrape(sell_url, 'sell')
scrape(rent_url, 'rent')