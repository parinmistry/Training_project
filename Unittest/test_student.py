from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from time import sleep

class student(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_student(self):
        self.driver.get("http://localhost/e_learning/e_learning/")
        self.driver.find_element(By.CSS_SELECTOR, ".main-menu > li:nth-child(2) > a").click()
        sleep(3)
        self.driver.find_element(By.ID, "ui-id-2").click()
        sleep(3)
        self.driver.find_element(By.ID, "ui-id-3").click()
        sleep(3)
        


    def teardown(self):
        self.driver = webdriver.quit()

if __name__ =="__main__":
    unittest.main()


