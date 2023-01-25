from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCon
from selenium.webdriver.common.by import By
import discord
import requests
import time

def scrape_class(url):

    cCode = ''
    cName = ''
    iName = ''
    dayText = ''
    tStart = ''
    tEnd = ''
    cLoc = ''
    cSeats = ''

    o = Options()
    o.headless = True # it's more scalable to work in headless mode 
    # normally, selenium waits for all resources to download 
    # we don't need it as the page also populated with the running javascript code. 
    o.page_load_strategy = 'none'
    driver = webdriver.Firefox(options=o)
    wait = WebDriverWait(driver, 20)

    driver.get(url)
    try:
        wait.until(ExpCon.presence_of_element_located((By.CLASS_NAME, "class-results-rows")))
    except:
        embed=discord.Embed(title="Course Not Found", description="We ain't found shit!", color=0x00ff00)
        return embed

    time.sleep(0.5)

    src = driver.page_source

    tree = html.fromstring(src)

    time.sleep(5)

    results = tree.xpath('//*[@id="class-results"]')

    print (results)

    cCode = tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[1]/span/text()')
    cName = tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[2]/span/text()')
    iName = tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[5]/a/text()')
    dayText = tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[6]/p/text()')
    tStart= tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[8]/p/text()')
    tEnd= tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[10]/p/text()')
    cLoc = tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[11]/p/a/text()')
    cSeats = tree.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[5]/div/div/div/div[2]/div[14]/div/text()')

    print(cCode)
    
    embed = discord.Embed(title=f"{cCode[0]} - {cName[0]}", description=f"Course Details for selected course", color=0xffc627)
    embed.add_field(name='Course name', value=cName[0], inline=False)
    embed.add_field(name="Instructor", value=iName[0], inline=False)
    embed.add_field(name="Course Days", value=dayText[0], inline=False)
    embed.add_field(name="Start Time", value=tStart[0], inline=False)
    embed.add_field(name="End Time", value=tEnd[0], inline=False)
    embed.add_field(name="Location", value=cLoc[0], inline=False)
    embed.add_field(name="Seats Open", value=cSeats[0], inline=False)

    return embed