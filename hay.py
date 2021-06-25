from django.test import TestCase
from prac.models import Item, pendingname, Money, income

class TestHomePage(TestCase):

	def test_mainpage_returns_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'psrform.html')

class ORMTest(TestCase):
	def test_save_retrive_list(self):
		newName = pendingname()
		newName.save()
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.pname = newName
		txtItem1.address = 'address one'
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.pname = newName
		txtItem2.text = 'Item two'
		txtItem2.address = 'address two'
		txtItem2.save()
		savedItems = Item.objects.all()
		savedpendingname = pendingname.objects.first()
		self.assertEqual(savedItems.count(), 2)
		self.assertEqual(savedpendingname, newName)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')
		self.assertEqual(savedItem1.pname, newName)
		self.assertEqual(savedItem2.pname, newName)
		self.assertEqual(savedItem1.address, 'address one')
		self.assertEqual(savedItem2.address, 'address two')
	
	# def test_try_new_model(self):
	# 	money = income()
	# 	money.save()
	# 	moneytext1 = Money()
	# 	moneytext1.occu = 'occu one'
	# 	moneytext1.mney = money 
	# 	moneytext1.salary = 'salary one'
	# 	moneytext1.save()
	# 	moneytext2 = Money()
	# 	moneytext2.mney = money 
	# 	moneytext2.occu = 'occu two' 
	# 	moneytext1.salary = 'salary two'
	# 	moneytext2.save()
	# 	savedMoney = money.objects.all()
	# 	savedIncome = income.objects.first()
	# 	self.assertEqual(savedMoney.count(), 2)
	# 	self.assertEqual(savedincome, money)
	# 	savedtext1 = savedMoney[0]
	# 	savedtext2 = savedMoney[1]
	# 	self.assertEqual(savedtext1.occu, 'occu one')
	# 	self.assertEqual(savedtext2.occu, 'occu two')
	# 	self.assertEqual(savedtext1.mney, money)
	# 	self.assertEqual(savedtext2.mney, money)
	# 	self.assertEqual(savedtext1.salary, 'salary one')
	# 	self.assertEqual(savedtext2.salary, 'salary two')
	# 	#BAGO TO LAHAT TRY

class ViewingTest(TestCase):
	def test_displays_for_each_pendingname(self):
		newName = pendingname.objects.create()
		address = pendingname.objects.create() #ITO
		Item.objects.create(pname=newName, text='Liza') #palitan mamaya ang text dito at sa taas
		Item.objects.create(pname=newName, text='Gil')
		response = self.client.get(f'/prac/{newName.id}/')
		self.assertNotContains(response, 'Bernardo')
		self.assertNotContains(response, 'Padilla')

		newName_2 = pendingname.objects.create()
		Item.objects.create(pname=newName_2, text='Bernardo') #palitan mamaya ang text dito at sa taas
		Item.objects.create(pname=newName_2, text='Padilla')
		response = self.client.get(f'/prac/{newName_2.id}/')
		self.assertNotContains(response, 'Liza')
		self.assertNotContains(response, 'Gil')

	def test_listviewing_uses_listpage(self):
		newName = pendingname.objects.create()
		response = self.client.get(f'/prac/{newName.id}/')
		self.assertTemplateUsed(response, 'psrlist.html') #ITO PINALITAN KO HTML
   
	def test_pass_list_temp(self):
		subsidy1 = pendingname.objects.create()
		subsidy2 = pendingname.objects.create()
		passinglistahan = pendingname.objects.create()
		response = self.client.get(f'/prac/{passinglistahan.id}/')
		self.assertEqual(response.context['pn'], passinglistahan) #pasahan ng data

# #-----TRY YUNG BABA
# 	def test_displays_for_each_money(self):
# 		money = income.objects.create()
# 		address = income.objects.create() #ITO
# 		Money.objects.create(mney=money, occu='Liza') #palitan mamaya ang text dito at sa taas
# 		Money.objects.create(mney=money, occu='Gil')
# 		response = self.client.get(f'/prac/{money.id}/')
# 		self.assertNotContains(response, 'Bernardo')
# 		self.assertNotContains(response, 'Padilla')

# 		money_2 = income.objects.create()
# 		Money.objects.create(mney=money_2, occu='Bernardo') #palitan mamaya ang text dito at sa taas
# 		Money.objects.create(mney=money_2, occu='Padilla')
# 		response = self.client.get(f'/prac/{money_2.id}/')
# 		self.assertNotContains(response, 'Liza')
# 		self.assertNotContains(response, 'Gil')

# 	def test_listviewing_uses_listpage1(self):
# 		money = income.objects.create()
# 		response = self.client.get(f'/prac/{money.id}/')
# 		self.assertTemplateUsed(response, 'psrlist.html') #ITO PINALITAN KO HTML
   
# 	def test_pass_list_temp1(self):
# 		pera1 = income.objects.create()
# 		pera2 = income.objects.create()
# 		passingincome = income.objects.create()
# 		response = self.client.get(f'/prac/{passingincome.id}/')
# 		self.assertEqual(response.context['my'], passingincome) #pasahan ng data
# #------


class creatingnewlisttest(TestCase):
	
	def test_for_POST_request_to_save(self):
		response = self.client.post('/prac/newlist_url', data={'surname': 'sname','address' : 'address'})
		self.assertEqual(Item.objects.count(), 1) #^^wala talaga siyang / ha ghoourl
		newIt = Item.objects.first()
		self.assertEqual(newIt.text, 'sname')
		self.assertEqual(newIt.address, 'address')



# #new---
# 		response = self.client.post('/prac/newlist_url', data={'occu': 'occup', 'salary':'salary'})
# 		self.assertEqual(Money.objects.count(), 1)
# 		newMy = Money.objects.first()
# 		self.assertEqual(newMy.occu, 'occu')
# 		self.assertEqual(newMy.salary, 'salary') 
# #x-----




	def test_POST_redirect_go_roli(self):
		response = self.client.post('/prac/newlist_url',data={'surname': 'sname','address': 'address'})
		newName = pendingname.objects.first()
		self.assertRedirects(response, f'/prac/{newName.id}/') 



# #new----
# 	def test_POST_new_model_try(self):
# 		response = self.client.post('/prac/newlist_url',data={'occu': 'occup','salary': 'salary'})
# 		money = income.objects.first()
# 		self.assertRedirects(response, f'/prac/{money.id}/') 
# #-------



class addingofitem(TestCase):
	def test_add_POST_existing_list_request(self):
		ayuDa1 = pendingname.objects.create()
		ayuDa2 = pendingname.objects.create()
		existlist = pendingname.objects.create()
		self.client.post(f'/prac/{existlist.id}/addItem',data={'surname': 'New Item for existing list', 'address' : 'New address for existing list'})
		self.assertEqual(Item.objects.count(), 1)
		newIt = Item.objects.first()
		self.assertEqual(newIt.text, 'New Item for existing list')
		self.assertEqual(newIt.address, 'New address for existing list')
		self.assertEqual(newIt.pname, existlist)

# #new-----
# 		sweldo1 = income.objects.create()
# 		sweldo2 = income.objects.create()
# 		existlist = income.objects.create()
# 		self.client.post(f'/prac/{existlist1.id}/addItem',data={'occu': 'New Money for existing list1', 'salary' : 'New salary for existing list1'})
# 		self.assertEqual(Money.objects.count(), 1)
# 		newMy = Money.objects.first()
# 		self.assertEqual(newMy.occu, 'New Money for existing list')
# 		self.assertEqual(newMy.salary, 'New salary for existing list')
# 		self.assertEqual(newMy.mney, existlist1)
# #----


	def test_redirects_listview(self):
		ayuda1 = pendingname.objects.create()
		ayuda2 = pendingname.objects.create()
		ayuda3 = pendingname.objects.create()
		existlist = pendingname.objects.create()
		response = self.client.post(f'/prac/{existlist.id}/addItem',data={'surname': 'New Item for existing list','address' : 'New address for existing list'})
		self.assertRedirects(response, f'/prac/{existlist.id}/')


# #new------
# 		kwarta1 = income.objects.create()
# 		kwarta2 = income.objects.create()
# 		kwarta3 = income.objects.create()
# 		existlist1 = income.objects.create()
# 		response = self.client.post(f'/prac/{existlist1.id}/addItem',data={'occu': 'New Money for existing list','salary' : 'New salary for existing list'})
# 		self.assertRedirects(response, f'/prac/{existlist1.id}/')




#from django.urls import resolve
#from psr.views import MainPage
#from django.http import HttpRequest
#from django.template.loader import render_to_string


		# def test_save_necessary_items(self):
		# 	self.client.get('/')
		# 	self.assertEqual(Item.objects.count(), 0)

		# def test_displaying_template_list(self):
		# 	Item.objects.create(text='List item 1')
		# 	Item.objects.create(text='List item 2')
		# 	response = self.client.get('/')
		# 	self.assertIn('List item 1', response.content.decode())
		# 	self.assertIn('List item 2', response.content.decode())

		

		# self.assertEqual(response.status_code, 302)
		# self.assertEqual(response['location'], '/psr/viewlist_url/')






#PREVIOUS CODE FOR REFERENCE

	#self.assertIn('sname', response.content.decode())
		#self.assertIn('gname', response.content.decode())
		#self.assertTemplateUsed(response, 'psrform.html')


# 'middlename' : 'mname', 'age' : 'age', 'sex' : 'sex',
		# 'adress' : 'address'})
"""	
	def test_if_root_resolves_mainpage(self):
		found = resolve ('/')
		self.assertEqual(found.func, MainPage)

	def tes_mainpage_returns_view(self):
		response = self.client('/')
		html = response.content.decode('utf8')
		main_html = render_to_string('psrform.html')
		self.assertEqual(html, main_html)
		self.assertTemplateUsed(response, 'psrform.html')

	def test_mainpage_returns_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		string_html = render_to_string('psrform.html')
		self.assertEqual(html, string_html)

	def test_mainpage_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>Pandemic Subsidy Registration</title>', html)
		self.assertTrue(html.endswith('</html>'))
# Create your tests here. """
