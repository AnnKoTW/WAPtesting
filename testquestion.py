from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

class Testquestion:

	@staticmethod
	def test_selenium():
		#mobile_emulation
		chrome_options = webdriver.ChromeOptions()
		mobile_emulation={
			#"deviceName":"Nexus 5"
			#"deviceName": "iPhone SE"
			"deviceName": "Samsung Galaxy S20 Ultra"
		}
		chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

		driver=webdriver.Chrome(options=chrome_options)

		#steps 1
		driver.get("https://m.twitch.tv/")

		time.sleep(3)

		#steps 2
		driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/nav/div[3]/a').click()
		time.sleep(3)

		#steps 3
		driver.find_element_by_xpath('//*[@id="page-main-content-wrapper"]/nav/div/div/div[2]/div/div/input').send_keys('StarCraft II')
		driver.find_element_by_xpath('//*[@id="page-main-content-wrapper"]/nav/div/div/div[2]/div/div/input').send_keys(Keys.ENTER)

		time.sleep(3)

		#steps 4
		for _ in range(2):
			driver.execute_script("window.scrollBy(0,100);")
			time.sleep(1)

		#steps 5
		driver.find_element_by_xpath('//*[@id="page-main-content-wrapper"]/div/div/section[1]/div[4]/a/div').click()

		#steps 6
		WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/div[3]/a')))

		time.sleep(5)
		screenshot_path='screenshot.png'
		driver.save_screenshot(screenshot_path)

		driver.quit()