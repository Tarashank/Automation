# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time


driver = uc.Chrome()
driver.maximize_window()

#open page
url = "https://in.bookmyshow.com/"
driver.get(url)

#wait for load the page 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[3]/ul/li[9]/div/div/img")))

#select citie
kolkata = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[3]/ul/li[9]")
kolkata.click()

#open movie section
movie_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/header/div[2]/div/div/div/div[1]/div/a[1]")
movie_btn.click()
print("Movie secton open")
# Select movie
# WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/a[2]/div/div[2]/div/img"))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/a[2]/div/div[2]/div/img")))
sel_mov = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/a[2]/div/div[2]/div/img")
sel_mov.click()
print("Movie open")
#open movie booking page
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/div[2]/div/div/button/div")))
book_tc_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/div[2]/div/div/button/div")
book_tc_btn.click()
print("Booking open")
#open hall and time chossing page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/section[2]/div[3]/div/ul/li[3]/div[2]/div[2]/div[2]/a")))

# popup_notnow_btn = driver.find_element(By.XPATH, "/html/body/div[20]/div[2]/div[3]/button[1]")
# popup_notnow_btn.click()
# print("popout handel")
#select show time 
show_time = driver.find_element(By.XPATH, "/html/body/div[5]/section[2]/div[3]/div/ul/li[2]/div[2]/div[2]/div[1]/a")
show_time.click()
print("show time selected")

#select seat number
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[17]/strong/div[6]/div[2]/div[4]/div")))
select_seat_count = driver.find_element(By.XPATH, "/html/body/div[17]/strong/div[6]/div[2]/div[4]/div")
seat_count = driver.find_element(By.XPATH, "/html/body/div[17]/strong/div[6]/div[2]/div[2]/ul/li[2]")
seat_count.click()
select_seat_count.click()
print("seat count selected")

#Choose show time
time_btn = driver.find_element(By.XPATH, "/html/body/section/div[3]/header/div[4]/div/div/ul/li[2]")
time_btn.click()
print("Time slot selected")

#find avilable seats
available_seat = driver.find_elements(By.CLASS_NAME, "")



time.sleep(10)
print("payment page open")