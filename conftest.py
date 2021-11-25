import logging
import yaml
import pytest
import sys
from socket import gethostname
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def config():
	with open("config.yml") as config_yml:
		config = yaml.safe_load(config_yml)
	return config




@pytest.fixture
def driver(config):
	browser = config['browser']['name']
	if browser == "chrome":
		driver = webdriver.Chrome("C:/bin/chromedriver.exe")
		driver.get("http://localhost/elearn")
		driver.set_window_size(1552, 840)
	elif browser == "edge":
		driver = webdriver.Edge("C:/bin/msedgedriver.exe")
		driver.get("http://localhost/elearn")
		driver.set_window_size(1552, 840)
	else:
		raise Exception("unsupported browser")

	yield driver

	driver.quit()



