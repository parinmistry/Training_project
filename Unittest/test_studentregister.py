import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_studentregister(self):
        self.driver.get("http://localhost/e_learning/e_learning/")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > .external").click()
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()
        sleep(1)
        self.driver.find_element(By.ID, "fname").click()
        self.driver.find_element(By.ID, "fname").send_keys("Devang")
        self.driver.find_element(By.ID, "lname").click()
        self.driver.find_element(By.ID, "lname").send_keys("Thaker")
        sleep(1)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("devanga.thaker@gmail.com")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("9909822439")
        self.driver.find_element(By.ID, "male").click()
        sleep(1)
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("Dev123")
        sleep(1)   
        self.driver.find_element(By.ID, "re-password").click()
        self.driver.find_element(By.ID, "re-password").send_keys("Dev123")
        sleep(1)
                                                          
        self.driver.find_element(By.NAME, "submit").click()

    def teardown(self):
        self.driver = webdriver.quit()

if __name__ == "__main__":
	unittest.main()