from selenium import webdriver
from selenium.webdriver.chrome.service import Service


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

column_names = [
                'Регион', 'Район', 'Тип', 'Материал здания', 'Цена', 'Дата', 'Площадь','Цена м2', 'Кол. комнат', 
                'Этажность', 'Этаж', 'Описание', 'Лифт', 'Охрана', 'Интернет', 'Детская площадка', 'Сауна', 
                'Канализация', 'Холодильник', 'Телефонная линия', 'Санузел раздельный', 'Видеонаблюдение', 
                'Бассейн', 'Водоснабжение', 'Микроволновая печь', 'Парковочное место', 'Кондиционер', 'Телевизор',
                'Стиральная машина', 'Спутниковое/кабельное ТВ', 'Мебель', 'Газоснабжение',
               ]

sell_url = ("https://api.uybor.uz/api/v1/listings?mode=search&includeFeatured=true&limit=20&embed=category%2CsubCategory%"
       "2CresidentialComplex%2Cregion%2Ccity%2Cdistrict%2Czone%2Cstreet%2Cmetro%2Cmedia%2Cuser%2Cuser.avatar%2Cuser."
       "organization%2Cuser.organization.logo&order=upAt&operationType__eq=sale&priceCurrency__eq=usd&category__eq=7")

rent_url = ("https://api.uybor.uz/api/v1/listings?mode=search&includeFeatured=true&limit=20&embed=category%2CsubCategory%"
            "2CresidentialComplex%2Cregion%2Ccity%2Cdistrict%2Czone%2Cstreet%2Cmetro%2Cmedia%2Cuser%2Cuser.avatar%2Cuser."
            "organization%2Cuser.organization.logo&order=upAt&operationType__eq=rent&priceCurrency__eq=usd&category__eq=7")

facility_cols = column_names[12:]

service = Service(executable_path=r"C:/SeleniumDrivers/chromedriver.exe")
options= webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument('--log-level=3')

driver = webdriver.Chrome(service=service, options=options)