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

	def test_courses(self):
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > a").click()
		sleep(3)
		ff = self.driver.find_element(By.XPATH,"/html/body/section[5]/div/div/div[1]/div/h2").text
		assert ff =="Choose Your Course"

#pytest test_courses.py