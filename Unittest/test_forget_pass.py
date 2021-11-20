# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:45:23 2021

@author: Devang
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/bin/chromedriver.exe")

    def test_studentregister(self):
        self.driver.get("http://localhost/elearn/")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > .external").click()
        self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-warning").click()
        sleep(1)
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
        
    def teardown(self):
        self.driver = webdriver.quit()

if __name__ =="__main__":
    unittest.main()
