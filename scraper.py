from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome()
browser.get(START_URL)

scraped_data = []

def scrape():
        star_table = soup.find("table", attrs={"class", "wikitable"})
        table_body = star_table.find("tbody")
        table_rows = table_body.find_all("tr")

        for row in table_rows: 
            table_cols = row.find_all("td")
            print(table_cols)

            temp_list = []

            for col_data in table_cols:
                print(col_data.text)

                data = col_data.strip()
                print(data)

                temp_list.append(data)
        
        scraped_data.append(temp_list)

stars_data =[]

for i in range(0, len(scraped_data)):
     
     starnames = scraped_data[i][1]
     distance = scraped_data[i][3]
     mass = scraped_data[i][5]
     radius = scraped_data[i][6]
     lum = scraped_data[i][7]

     required_Data = [starnames, distance, mass, radius, lum]
     stars_data.append(required_Data)

headers = ['star name', 'distance', 'mass', 'radius', 'luminosity']
star_df_1 = pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv('scrapeddata.csv', index = True, index_label='id')

