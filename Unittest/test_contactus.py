import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Faculty(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_contactus(self):
        self.driver.get("http://localhost/e_learning/e_learning/")
        self.driver.set_window_size(1536, 824)
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) > a").click()
        sleep(1)
        self.driver.find_element(By.ID, "name").send_keys("Parin Mistry")
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 #email").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 #email").send_keys("parinmistry789@gmail.com")
        self.driver.find_element(By.ID, "message").click()
        self.driver.find_element(By.ID, "message").send_keys("Feedback is good for website!")
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 > #contact #form-submit").click()
  
    def teardown(self):
        self.driver = webdriver.quit()
        
if __name__ == "__main__":
	unittest.main()

