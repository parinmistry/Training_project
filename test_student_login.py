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
		self.fake = Faker()

	def test_student_login(self):
		log.info("Test is started")
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > .external").click()
		self.driver.find_element(By.NAME, "email").send_keys("ghanist@gnu.ac.in")
		self.driver.find_element(By.NAME, "pass").click()
		self.driver.find_element(By.NAME, "pass").send_keys("parinmistry789")
		self.driver.find_element(By.ID, "signin").click()
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) p").click()
		sleep(1)
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) p").click()
		sleep(1)
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) p").click()
		sleep(1)
		assert self.driver.find_element(By.CSS_SELECTOR,".login100-form-title").text == "Student Login"
		log.info("Test is Successful")