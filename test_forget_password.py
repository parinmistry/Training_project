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
		
	def test_password(self):
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > .external").click()
		self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-warning").click()
		self.wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR,"body > div > form > div")))
		self.driver.find_element(By.NAME, "email").click()
		self.driver.find_element(By.NAME, "email").send_keys("devanga.thaker@gmail.com")
		sleep(1)
		self.driver.find_element(By.NAME, "npass").click()
		self.driver.find_element(By.NAME, "npass").send_keys("dev345")
		sleep(1)
		self.driver.find_element(By.NAME, "cpass").click()
		self.driver.find_element(By.NAME, "cpass").send_keys("dev345")
		sleep(1)
		self.driver.find_element(By.NAME, "submit").click()

#pytest test_forget_password.py