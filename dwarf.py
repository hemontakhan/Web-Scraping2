from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
PAGE_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(PAGE_URL)
soup = BeautifulSoup(page.text,'html.parser')
star_table = soup.find_all('table')
star_rows = star_table[7].find_all('tr')

def scrape():
  columns = ['Star','Constellation','Rightascension','Declination'	,'App.','mag.','Distance (ly)','Spectral type','Brown dwarf	 Mass(MJ)','Radius(RJ)','Orbital','period(d)','Semimajor','axis','(AU)','Ecc.','Discovery year',]
  final_dwarf_data = []
  for tr_tag in soup.find_all("tr"):
        td_tags = tr_tag.find_all("td")
  final_dwarf_data.append(td_tags)        

  with open('dwarf_stars.csv',"w") as r:
    csvwriter = csv.writer(r)
    csvwriter.writerow(columns)
    csvwriter.writerows(final_dwarf_data)

scrape()