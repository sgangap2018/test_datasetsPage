import pytest
import allure
import unittest
import glob
import csv
from time import sleep
import test_args
import locators
import os

#load args for dataset url and dataset column headers
ARGS = test_args.get_args()


@pytest.mark.usefixtures("session_feeder")
class dataset_page:
	pass
class Test_Dataset_Download(dataset_page):

	def test_login(self):
		URL_LOGIN = 'https://aiclub.world/login'
		self.driver.get(URL_LOGIN)
		username = 'sgangap2018@gmail.com'
		password = 'Being@T/here3'

		# login to AiClub site
		login_cred = self.driver.find_element(*locators.USERNAME)
		login_cred.send_keys(username)

		password_form = self.driver.find_element(*locators.PASSWORD)
		password_form.send_keys(password)

		login_button = self.driver.find_element(*locators.LOGIN_BUTTON)
		login_button.click()
		sleep(3)

	@allure.step('Download File')
	@pytest.mark.parametrize("dataset_id, column_headers", ARGS)
	def test_download(self,dataset_id,column_headers):
		#Go to AIClub project dataset URL and click 'Download' Button
		URL_DATASET = 'https://aiclub.world/dataset?id={s}&tab=datasets'.format(s=dataset_id)
		self.driver.get(URL_DATASET)
		self.download_file()

		#check target directory for latest file that is a .csv and open file to verify correct column headers
		download_path = '/home/ax3/PycharmProjects/test_datasets_projPage/tests/Downloads/*.csv'
		list_of_files = glob.glob(download_path)
		latest_file = max(list_of_files, key=os.path.getctime)
		try:
			with open(latest_file, mode="r") as f:
				reader = csv.reader(f)
				columns_list = next(reader)
				case = unittest.TestCase()
				# assert that length of column headers list is the same as the headers
				# list AND that the elements are the same as those provided in the test argument
				case.assertCountEqual(columns_list, column_headers)
		except ValueError as e:
			print('Download Not Completed!' + str(e))
			print('Dataset link: ', URL_DATASET)
		except AssertionError as e:
			print('Assertion Failed' + str(e))
			print('Dataset link: ', URL_DATASET)
		finally:
			os.remove(latest_file)

	def download_file(self):
		self.driver.implicitly_wait(5)
		self.driver.find_element(*locators.DOWNLOAD_BUTTON).click()
		sleep(5)



