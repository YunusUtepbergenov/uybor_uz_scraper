import requests
import pandas as pd
from bs4 import BeautifulSoup
from math import ceil
from data.variables import column_names, headers, facility_cols, driver

def scrape(url, type):
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    total_apts = int(data['total'])
    total_pages = ceil(total_apts / 20)
    dataframe = pd.DataFrame(columns=column_names)
    row = 1

    for page in range(total_pages):
        print("Page is " + str(page + 1) + "/" + str(total_pages))
        href = url + '&page=' + str(page + 1)
        response = requests.request("GET", href, headers=headers)
        data = response.json()
        houses = data['results']

        for house in houses:
            try:    
                dataframe.at[row, 'Регион'] = house['region']['name']['ru']
                dataframe.at[row, 'Район'] = house['district']['name']['ru']
                dataframe.at[row, 'Тип'] = house['category']['name']['ru']
                dataframe.at[row, 'Материал здания'] = house['foundation']
                dataframe.at[row, 'Цена'] = house['price']
                dataframe.at[row, 'Дата'] = house['createdAt']
                dataframe.at[row, 'Площадь'] = house['square']
                dataframe.at[row, 'Цена м2'] = float(house['price']) / float(house['square'])
                dataframe.at[row, 'Кол. комнат'] = house['room']
                dataframe.at[row, 'Этажность'] = house['floorTotal']            
                dataframe.at[row, 'Этаж'] = house['floor']
                dataframe.at[row, 'Описание'] = house['description']

                driver.get("https://uybor.uz/listings/" + str(house['id']))
                html_page = driver.page_source
                soup = BeautifulSoup(html_page, 'lxml')

                facility = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-4 MuiGrid-grid-lg-3 mui-style-1ehnifu')
                if facility:
                    facility_items = facility.find_all('div', class_="MuiTypography-root MuiTypography-body3 mui-style-xckitu")
                    for item in facility_items:
                        if item.text in column_names:
                            dataframe.at[row, item.text] = True
            except:
                continue
            row = row + 1
    
    dataframe[facility_cols] = dataframe.loc[:,facility_cols].fillna(value=False)
    dataframe.dropna(subset=['Цена', 'Площадь', 'Кол. комнат', 'Этаж'])
    dataframe.to_excel("results/uybor_" + type + ".xlsx", index=False)