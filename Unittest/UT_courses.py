import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Faculty(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    
    def test_student(self):
        self.driver.get("http://localhost/elearn/")
        self.driver.set_window_size(1340, 824)
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > a").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".owl-item:nth-child(9) .down-content")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".owl-item:nth-child(9) .down-content")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".owl-item:nth-child(9) .down-content")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".owl-item:nth-child(9) .down-content").click()
        text = self.driver.find_element(By.CSS_SELECTOR, ".owl-item:nth-child(5) h4").text
        assert text == "OPERATING SYSTEM"

    def teardown(self):
        self.driver = webdriver.quit()

if __name__ == "__main__":
	unittest.main()