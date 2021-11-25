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
	def faculty_account(self):
		faculty_account = SimpleNamespace()
		faculty_account.first_name = self.fake.first_name()
		faculty_account.last_name = self.fake.last_name()
		faculty_account.email = self.fake.email()
		faculty_account.age ="50"
		faculty_account.qualification = "B.Tech"
		faculty_account.exp = "5 years"
		faculty_account.number = "7878787878"
		faculty_account.password = "OK_GOOGLE"
		self.faculty_account = faculty_account
		return faculty_account

	
	def test_navigate_to_become_faculty(self):
		gender_text = By.CSS_SELECTOR, ".row:nth-child(5) > .col-md-6:nth-child(2) label:nth-child(1)"
		hover_element = By.CSS_SELECTOR, "li.has-submenu"
		become_faculty=By.CSS_SELECTOR, "li:nth-child(1) > .external"
		self.driver.find_element(*hover_element).click()
		self.driver.find_element(*become_faculty).click()
		assert self.driver.find_element(*gender_text).text == "Gender"
		

	def test_form_filling(self,faculty_account):
		self.test_navigate_to_become_faculty()
		self.driver.find_element(By.ID, "fname").send_keys(faculty_account.first_name)
		self.driver.find_element(By.ID, "lname").click()
		self.driver.find_element(By.ID, "lname").send_keys(faculty_account.last_name)
		sleep (2)
		self.driver.find_element(By.ID, "email").click()
		self.driver.find_element(By.ID, "email").send_keys(faculty_account.email)
		self.driver.find_element(By.ID, "age").click()
		self.driver.find_element(By.ID, "age").send_keys(faculty_account.age)
		sleep (2)
		self.driver.find_element(By.ID, "qualify").click()
		self.driver.find_element(By.ID, "qualify").send_keys(faculty_account.qualification)
		self.driver.find_element(By.ID, "experience").click()
		self.driver.find_element(By.ID, "experience").send_keys(faculty_account.exp)
		self.driver.find_element(By.NAME, "phone").click()
		self.driver.find_element(By.NAME, "phone").send_keys(faculty_account.number)
		sleep (1)
		self.driver.find_element(By.ID, "male").click()
		self.driver.find_element(By.ID, "re-password").click()
		self.driver.find_element(By.ID, "re-password").send_keys(faculty_account.password)
		self.driver.find_element(By.ID, "password").click()
		self.driver.find_element(By.ID, "password").send_keys(faculty_account.password)
		sleep (1)
		self.driver.find_element(By.NAME, "submit").click()
		heading = self.driver.find_element(By.CSS_SELECTOR,"header > div >a").text
		assert heading =="MIND WAVE"
	
	






