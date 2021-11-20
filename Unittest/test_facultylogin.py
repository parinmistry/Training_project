import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class Faculty(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_LoginFaculty(self):
        self.driver.get("http://localhost/e_learning/e_learning/index.php")
        sleep(2)
        self.driver.set_window_size(1536, 824)
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
        assert self.driver.find_element(By.CSS_SELECTOR, ".head").text == "MINDWAVE"

    def teardown(self):
        self.driver = webdriver.quit()
        
if __name__ == "__main__":
	unittest.main()

