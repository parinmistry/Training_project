import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



class student(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_studentlogin(self):
        self.driver.get("http://localhost/e_learning/e_learning/")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > .external").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("ghanist@gnu.ac.in")
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys("ghanist@123")
        self.driver.find_element(By.ID, "signin").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) p").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) p").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) p").click()
        sleep(1)

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main()
