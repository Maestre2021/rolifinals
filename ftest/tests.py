from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3

class FrontPage(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	# def tearDown(self):
	# 	self.browser.quit()

	def wait_rows_list(self, row_text):
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.2)
			try:
				table = self.browser.find_element_by_id('psrtable')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return 
			except (AssertionError, WebDriverException) as e:
				if time.time()-start_time>cWait:
					raise e

	def test_start_one_user(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Pandemic Subsidy Registration', self.browser.title)
		Mainheader = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Pandemic Subsidy form', Mainheader)

		surname = self.browser.find_element_by_id('surname')
		surname.click()
		surname.send_keys('Maestre, Roli Anne A.')
		time.sleep(.1)

		age = self.browser.find_element_by_id('age')
		age.click()
		age.send_keys('21')
		time.sleep(.1)
		

		female = self.browser.find_element_by_id('fsex')
		female.click()
		time.sleep(.1)

		address = self.browser.find_element_by_id('address')
		address.send_keys('Block 232 Lot 7 Phase 2 Mabuhay City Paliparan 3 Dasmarinas City, Cavite')
		time.sleep(.1)
		address.send_keys(Keys.ENTER)

		confirmbtn = self.browser.find_element_by_id('confirmbtn')
		confirmbtn.click()
		self.wait_rows_list("1: Maestre, Roli Anne A. Block 232 Lot 7 Phase 2 Mabuhay City Paliparan 3 Dasmarinas City, Cavite")

# ------------------------------------------------------------------------------
		surname = self.browser.find_element_by_id('surname')
		surname.click()
		surname.send_keys('Sabalboro, Mike Nyl S.')
		time.sleep(1)

	
		age = self.browser.find_element_by_id('age')
		age.click()
		age.send_keys('21')
		time.sleep(1)
		

		female = self.browser.find_element_by_id('msex')
		female.click()
		time.sleep(1)

		address = self.browser.find_element_by_id('address')
		address.send_keys('Block 323 Lot 14 Phase 2 Mabuhay City Paliparan 3 Dasmarinas City, Cavite')
		time.sleep(1)

		confirmbtn = self.browser.find_element_by_id('confirmbtn')
		confirmbtn.click()
		self.wait_rows_list("2: Sabalboro, Mike Nyl S. Block 323 Lot 14 Phase 2 Mabuhay City Paliparan 3 Dasmarinas City, Cavite")



#---new

	def test_other_user_diff_urls(self):
		self.browser.get(self.live_server_url)
		time.sleep(.1)

		surname = self.browser.find_element_by_id('surname')
		surname.click()
		surname.send_keys('Lustre, Nadine')
		time.sleep(.1)

		age = self.browser.find_element_by_id('age')
		age.click()
		age.send_keys('21')
		time.sleep(.1)
		

		female = self.browser.find_element_by_id('fsex')
		female.click()
		time.sleep(.1)

		address = self.browser.find_element_by_id('address')
		address.send_keys('Block 15 lot 1 Phase 3 Mabuhay City Paliparan 3 Dasmarinas City, Cavite')
		time.sleep(.1)
		address.send_keys(Keys.ENTER)

		confirmbtn = self.browser.find_element_by_id('confirmbtn')
		confirmbtn.click()
		self.wait_rows_list('1: Lustre, Nadine Block 15 lot 1 Phase 3 Mabuhay City Paliparan 3 Dasmarinas City, Cavite') 
		viewlist_url = self.browser.current_url
		self.assertRegex(viewlist_url, '/prac/.+')


		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		bodypage = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Lustre', bodypage)
		time.sleep(.1)

		surname = self.browser.find_element_by_id('surname')
		surname.click()
		surname.send_keys('Reid, James')
		time.sleep(.1)


		age = self.browser.find_element_by_id('age')
		age.click()
		age.send_keys('25')
		time.sleep(1)
		

		female = self.browser.find_element_by_id('msex')
		female.click()
		time.sleep(1)

		address = self.browser.find_element_by_id('address')
		address.send_keys('Block 71 Lot 83 Phase 3 Mabuhay City, Paliparan 3 Dasmarinas City Cavite')
		time.sleep(1)

		confirmbtn = self.browser.find_element_by_id('confirmbtn')
		confirmbtn.click()

		self.wait_rows_list('1: Reid, James Block 71 Lot 83 Phase 3 Mabuhay City, Paliparan 3 Dasmarinas City Cavite')
		user2_url = self.browser.current_url
		self.assertRegex(user2_url, '/prac/.+')
		self.assertNotEqual(viewlist_url, user2_url)
		bodypage = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Lustre', bodypage)
		self.assertIn('Reid', bodypage)
 


		# table = self.browser.find_element_by_id('psrtable')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertIn(row_text, [row.text for row in rows])
		
		# table = self.browser.find_element_by_id('psrtable')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertIn('1. Maestre in Roli Anne', [row.text for row in rows])
		# self.assertIn('1. Sabalboro in Mike Nyl', [row.text for row in rows])

		# self.check_rows_list('2. Maestre, Roli Anne of Mabuhay City')



		# psrtable = self.browser.find_element_by_id('psrtable')
		# rows = psrtable.find_element_by_tag_name('tr')



		# def test_browser_title(self):
		# 	self.browser.get('http://localhost:8000')
		# 	self.assertIn('Pandemic Subsidy Registration', self.browser.title)
		# 	#self.fail('Where is your CV?!')

		# def test_start_checking_of_html(self):
		# 	self.browser.get('http://localhost:8000')
		# 	#self.assertIn('Pandemic Subsidy Registration', self.browser.title)
		# 	MainHeader = self.browser.find_element_by_tag_name('h1').text
		# 	self.assertIn('Pandemic Subsidy form', MainHeader)

		# table = self.browser.find_element_by_id('formtable')
		# rows = table.find_element_by_tag_name('tr')
		# self.assertTrue(any(row.text == 'Roli Anne'))
		# self.fail('Finish the form')

	"""def tearDown(self):
		self.browser.quit()

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Pandemic Subsidy Registration', self.browser.title)
		#self.fail('Where is your CV?!')



		{% csrf_token %}
</form>"""


# if __name__== '__main__':
# 	unittest.main(warnings='ignore')
