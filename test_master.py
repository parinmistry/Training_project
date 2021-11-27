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
		if self.driver.find_element(By.CSS_SELECTOR,"div > h3").text == "Register":
			log.info("test navigate to student register passed")
		else:
			log.info("test navigate to student register failed")

	@pytest.mark.register
	def test_student_register(self,student_account):
		self.test_navigate_to_student_register()
		self.wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR,"h3")))
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

	def test_student_login(self):
		log.info("test_student_login started")
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

	def test_student(self):
		log.info()
		self.driver.get("http://localhost/elearn/")
		self.driver.find_element(By.CSS_SELECTOR, ".main-menu > li:nth-child(2) > a").click()
		sleep(3)
		self.driver.find_element(By.ID, "ui-id-2").click()
		self.wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR,"#tabs-2 > div > div:nth-child(2) > h4")))
		self.driver.find_element(By.ID, "ui-id-3").click()
		self.wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR,"#tabs-3 > div > div:nth-child(2) > h4")))

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

	def test_faculty_login(self):
		self.driver.find_element(By.CSS_SELECTOR, "li.has-submenu").click()
		sleep(2)
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .external").click()
		self.driver.find_element(By.NAME, "email").click()
		self.driver.find_element(By.NAME, "email").send_keys("dhanvishah19@gmail")
		self.driver.find_element(By.NAME, "pass").click()
		self.driver.find_element(By.NAME, "pass").send_keys("abc123")
		self.driver.find_element(By.NAME, "pass").send_keys(Keys.ENTER)
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) p").click()
		sleep(1)
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) p").click()
		sleep(1)
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) p").click()
		sleep(1)
		assert self.driver.find_element(By.CSS_SELECTOR, ".logo").text == "MW\nMINDWAVE"

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

	def test_courses(self):
		self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > a").click()
		sleep(3)
		ff = self.driver.find_element(By.XPATH,"/html/body/section[5]/div/div/div[1]/div/h2").text
		self.driver.get_screenshot_as_file('test_courses.png')
		assert ff == "Choose Your Course"
