import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


class Faculty(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_BecomeFaculty(self):
        self.driver.get("http://localhost/elearn/")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.CSS_SELECTOR,"li.has-submenu").click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .external").click()
        self.driver.find_element(By.ID, "fname").click()
        sleep(2)
        self.driver.find_element(By.ID, "fname").send_keys("Example")
        self.driver.find_element(By.ID, "lname").click()
        self.driver.find_element(By.ID, "lname").send_keys("Test")
        self.driver.find_element(By.ID, "email").click()
        sleep(2)
        self.driver.find_element(By.ID, "email").send_keys("parinmistry789@gmail.com")
        self.driver.find_element(By.ID, "age").click()
        self.driver.find_element(By.ID, "age").send_keys("40")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4)").click()
        self.driver.find_element(By.ID, "qualify").click()
        self.driver.find_element(By.ID, "qualify").send_keys("B.E")
        self.driver.find_element(By.ID, "experience").click()
        self.driver.find_element(By.ID, "experience").send_keys("5 years")
        self.driver.find_element(By.NAME, "phone").click()
        sleep(2)
        self.driver.find_element(By.NAME, "phone").send_keys("7874094425")
        self.driver.find_element(By.ID, "female").click()
        self.driver.find_element(By.ID, "re-password").click()
        self.driver.find_element(By.ID, "re-password").send_keys("exampletest")
        self.driver.find_element(By.ID, "password").click()
        sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("exampletest")
        self.driver.find_element(By.NAME, "submit").click()
        print(self.driver.title)
        self.assertEqual(self.driver.title,"Sign Up #2")
        
    def teardown(self):
        self.driver = webdriver.quit()
        
if __name__ == "__main__":
	unittest.main()

