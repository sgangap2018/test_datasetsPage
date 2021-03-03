import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import glob
import os
import sys
import csv
import pandas as pd
from time import sleep
import tempfile
import shutil
import test_args

#load args for dataset url and dataset column headers
ARGS = test_args.get_args()

@pytest.mark.usefixtures("session_feeder")
class dataset_page:
	pass
class Test_Dataset(dataset_page):

	def test_login(self):
		URL_LOGIN = 'https://aiclub.world/login'
		self.driver.get(URL_LOGIN)
		username = 'sgangap2018@gmail.com'
		password = 'New@pw11'

		# login to AiClub site
		login_cred = self.driver.find_element_by_xpath("//input[@id='email']")
		login_cred.send_keys("sgangap2018@gmail.com")

		password_form = self.driver.find_element_by_xpath("//input[@id='password']")
		password_form.send_keys("New@pw11")

		login_button = self.driver.find_element_by_xpath("//div[@id='app']/div/main/div/form/button/span")
		login_button.click()
		sleep(3)

	@pytest.mark.parametrize("ids, column_headers", ARGS)
	def test_download(self,ids,column_headers):
		URL_DATASET = 'https://aiclub.world/dataset?id={s}&tab=datasets'
		self.driver.get(URL_DATASET.format(s=ids))
		self.download_file()
		try:
			self.check_download(column_headers)
		except:
			print('*.csv file not found')

	def download_file(self):
		self.driver.implicitly_wait(5)
		self.driver.find_element_by_xpath("//div[@id='app']/div/main/div/div/div[2]/button/span/p").click()
		sleep(5)

	def verify_download(self,columns):
		list_of_files = glob.glob('/home/ax3/PycharmProjects/test_datasets_projPage/tests/Downloads/*.csv')
		latest_file = max(list_of_files, key=os.path.getctime)
		with open(''.format(latest_file), "rb") as f:
			reader = csv.reader(f)
			i = reader.next()
			rest = list(reader)
			assert rest == columns
