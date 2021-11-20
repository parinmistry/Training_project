import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_studentregister(self):
        self.driver.get("http://localhost/elearn/")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > .external").click()
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()
        self.driver.find_element(By.ID, "fname").click()
        sleep(2)
        self.driver.find_element(By.ID, "fname").send_keys("Parin")
        self.driver.find_element(By.ID, "lname").click()
        self.driver.find_element(By.ID, "lname").send_keys("Mistry")
        self.driver.find_element(By.ID, "email").click()
        sleep(2)
        self.driver.find_element(By.ID, "email").send_keys("parinmistry789@gmail.com")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("8888777744")
        self.driver.find_element(By.ID, "male").click()
        self.driver.find_element(By.ID, "re-password").click()
        sleep(2)
        self.driver.find_element(By.ID, "re-password").send_keys("parin")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("parin")
        self.driver.find_element(By.NAME, "submit").click()

    def teardown(self):
        self.driver = webdriver.quit()

if __name__ == "__main__":
	unittest.main()