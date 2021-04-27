import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope='class')
def session_feeder(request):
	#specify download target directory
	prefs = {'download.default_directory': '/home/ax3/PycharmProjects/test_datasets_projPage/tests/Downloads'}

	#Chrome preferences, browser runs headlessly
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option('prefs', prefs)
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1440, 900")
	capabilities = chrome_options.to_capabilities()
	#driver = webdriver.Remote(command_executor='http://172.17.0.1:4444',desired_capabilities=capabilities)
	driver = webdriver.Chrome(desired_capabilities=capabilities)
	request.cls.driver = driver
	yield
	driver.quit()
