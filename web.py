from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://lvr.land.moi.gov.tw/")
chrome.switch_to.frame(0)

select_option1 = Select(chrome.find_element_by_id("p_city"))  # 選擇縣市
select_option1.select_by_value("A")  # 台北市
time.sleep(3)
select_option2 = Select(chrome.find_element_by_id("p_town"))  # 選擇鄉鎮市區
select_option2.select_by_value("A13")  # 南港區
checkbox1 = Select(chrome.find_element_by_id("customCheck2"))
checkbox1.click()  # 打勾土地


time.sleep(20)
