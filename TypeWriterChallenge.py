import time 

from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait

driver = webdriver.Chrome()

driver.get("http://play.typeracer.com/")

StartGame = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector('#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a'))
StartGame.click()

TextBox = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector('.inputPanel > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1)'))
InputBox = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input'))

print(InputBox)
time.sleep(15)

for i in range(len(TextBox.text.split())):
	print('Sending: {}'.format(TextBox.text.split()[i]))
	InputBox.send_keys(str(TextBox.text.split()[i]))
	if not i == len(TextBox.text.split()):
		InputBox.send_keys(' ')
	else:
		break
	time.sleep(0.05)

driver.quit()