from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import discord
import requests

def scrape(url):
    o = Options()
    o.add_argument('--headless')
    driver = webdriver.Firefox(options=o)

    driver.get(url)
    src = driver.page_source

    tree = html.fromstring(src)

    results = tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[14]')

    for course in results:
        openSeats = course.xpath('./div/text()')

    if results:
        return 1
    
    return 0