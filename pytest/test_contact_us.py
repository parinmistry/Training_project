import logging 
import sys
from time import sleep
from faker.proxy import Faker
from selenium import webdriver
from types import SimpleNamespace
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import pytest

logging.basicConfig()
log = logging.getLogger("elearn")
log.setLevel(logging.DEBUG)
log.addHandler(logging.FileHandler("elearn.log"))
log.addHandler(logging.StreamHandler(sys.stdout))


class Test_Elearning:

	@pytest.fixture(autouse=True)
	def setup(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)
	
	def test_contact_us(self):
		log.info("Test Contact Us")
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) > a").click()
		self.driver.find_element(By.XPATH,"/html/body/section[6]/div/div/div[1]/form/div/div[1]/fieldset/input").send_keys("Parin Mistry")
		sleep(2)
		self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 #email").click()
		self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 #email").send_keys("parinmistry789@gmail.com")
		sleep(2)
		self.driver.find_element(By.ID, "message").click()
		self.driver.find_element(By.ID, "message").send_keys("Feedback is good for website!")
		sleep(3)
		self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 > #contact #form-submit").click()
		assert self.driver.find_element(By.CSS_SELECTOR,".caption > h6").text == "MINDWAVE"
		log.info("is successful")

	#pytest test_contact_us.py

