from logging import log
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

class Test_Elearning:

	@pytest.fixture(autouse=True)
	def setup(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)
		self.fake = Faker()

	@pytest.fixture
	def student_account(self):
		student_account = SimpleNamespace()
		student_account.first_name = self.fake.first_name()
		student_account.last_name = self.fake.last_name()
		student_account.email = self.fake.email()
		student_account.number = self.fake.phone_number()
		student_account.password = "OK_GOOGLE"
		self.student_account = student_account
		return student_account
		
	def test_navigate_to_student_register(self):
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > .external").click()
		self.driver.find_element(By.LINK_TEXT, "Sign Up").click()
		sleep(1)
		assert self.driver.find_element(By.CSS_SELECTOR,"div > h3").text == "Register"

	def test_student_register(self,student_account):
		self.test_navigate_to_student_register()
		self.driver.find_element(By.ID, "fname").click()
		self.driver.find_element(By.ID, "fname").send_keys(student_account.first_name)
		self.driver.find_element(By.ID, "lname").click()
		self.driver.find_element(By.ID, "lname").send_keys(student_account.last_name)
		sleep(1)
		self.driver.find_element(By.ID, "email").click()
		self.driver.find_element(By.ID, "email").send_keys(student_account.email)
		self.driver.find_element(By.NAME, "phone").click()
		self.driver.find_element(By.NAME, "phone").send_keys(student_account.number)
		self.driver.find_element(By.ID, "male").click()
		sleep(1)
		self.driver.find_element(By.ID, "password").click()
		self.driver.find_element(By.ID, "password").send_keys(student_account.password)
		sleep(1)   
		self.driver.find_element(By.ID, "re-password").click()
		self.driver.find_element(By.ID, "re-password").send_keys(student_account.password)
		sleep(1)                                                
		self.driver.find_element(By.NAME, "submit").click()
		assert self.driver.find_element(By.CSS_SELECTOR,"div > h3").text == "Register"