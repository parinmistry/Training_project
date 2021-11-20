import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

class Faculty(unittest.TestCase):

    def setUp(self):
         self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_LoginFaculty(self):
        self.driver.get("http://localhost/elearn/")
        sleep(2)
        self.driver.set_window_size(1536, 824)
        self.driver.find_element(By.CSS_SELECTOR,"li.has-submenu").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .external").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("parinmistry789@gmail.com")
        self.driver.find_element(By.NAME, "pass").click()
        sleep(2)
        self.driver.find_element(By.NAME, "pass").send_keys("parinmistry789")
        self.driver.find_element(By.NAME, "pass").send_keys(Keys.ENTER)
        assert self.driver.find_element(By.CSS_SELECTOR, ".head").text == "MINDWAVE"

    def teardown(self):
        self.driver = webdriver.quit()
        
if __name__ == "__main__":
	unittest.main()

