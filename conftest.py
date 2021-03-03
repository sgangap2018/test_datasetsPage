import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import tempfile
import shutil


@pytest.fixture(scope='class')
def session_feeder(request):
	#create temporary directory for download target

	prefs = {'download.default_directory': '/home/ax3/PycharmProjects/test_datasets_projPage/tests/Downloads'}
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option('prefs', prefs)
	capabilities = chrome_options.to_capabilities()
	driver = webdriver.Remote(command_executor='http://172.17.0.1:4444',desired_capabilities=capabilities)
	request.cls.driver = driver
	yield
	driver.quit()