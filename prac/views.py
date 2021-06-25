from django.shortcuts import render, redirect
from prac.models import Psrsignup, Familyinfo, Subsidyconfirmation, Receivingplacedate, Receivingbankpawnshop, Inquries
# from .forms import PlaceForm



def Main(request):
	return render(request, 'psrform.html')


def Mainget(request ):
	pnames = Psrsignup.objects.create(
		completename =request.POST['completename'],
		address = request.POST['address'],
		salaryhead = request.POST['salary'],
		occupationhead = request.POST['occupation'],
		)

	familys = Familyinfo.objects.create(
		familyname1 = request.POST['Fullname1'],
		familyname2 = request.POST['Fullname2'],
		familyname3 = request.POST['Fullname3'],

		occupation1 = request.POST['occupation1'],
		occupation2 = request.POST['occupation2'],
		occupation3 = request.POST['occupation3'],


		salary1 = request.POST['salary1'],
		salary2 = request.POST['salary2'],
		salary3 = request.POST['salary3'],
		totalsalary = request.POST['totalsalary'],
		)

	return redirect('Subsidy')
	return render(request, 'subsidypage.html')

def Subsidy(request):
	# pname = Psrsignup.objects.filter()
	# family = Familyinfo.objects.all()


	# context = {'pname':pname , 'family':family }
	return render(request, 'subsidypage.html')

def Subsidyget(request):

	totals = Subsidyconfirmation.objects.create(
		subsidy = request.POST['expectedsubsidy'],
		contact = request.POST['number'],

		)	

	stations = Receivingplacedate.objects.create(
		place = request.POST['station'],
		date = request.POST['stationdate'],
		time = request.POST['stationtime'],

		)
	banks = Receivingbankpawnshop.objects.create(
		bank_pawnshop = request.POST['banks'],
		date = request.POST['bankdate'],
		time = request.POST['banktime'],
		)


	return redirect('Status')
	return render(request, 'subsidypage.html')





def Status(request):
	pname = Psrsignup.objects.last
	total = Subsidyconfirmation.objects.last
	station = Receivingplacedate.objects.last
	bank = Receivingbankpawnshop.objects.last
	family = Familyinfo.objects.last

	context = {'pname':pname, 'family': family,'station':station, 'bank':bank, 'total': total}
	return render(request, 'statuspage.html', context)

def Applicant(request):

	return render(request,'applicantpage.html')

def Aboutus(request):

	return render(request,'aboutus.html')


def Inquiriesandco(request):
	return render(request,'inquiriesandcomments.html')



def Inquire(request):

	inq = Inquries.objects.create(
		iname = request.POST['nameinquiries'],
		icontact = request.POST['contactinquiries'],
		typemessage = request.POST['typemessage'],
		comments = request.POST['message'],
		rate = request.POST['rate'],
		)

	return redirect('Inquiries')
	return render(request, 'inquiriesandcomments.html')

def Inquiries(request):


	inq = Inquries.objects.all()

	return render(request,'inquiriesandcomments.html', {'inq': inq})










def Home(request):
	return render(request, 'psrform.html')



def EditPlace(request, id):
	station = Receivingplacedate.objects.get(id=id)
	context = {'station':station}
	return render(request, 'editplace.html', context)


def UpdatePlace(request, id):
	station = Receivingplacedate.objects.get(id=id)
	station.place = request.POST['station']
	station.time = request.POST['stationtime']
	station.date = request.POST['stationdate']
	station.save ()
	return redirect('Status')

def DeletePlace(request, id):
	station = Receivingplacedate.objects.get(id=id)
	station.delete()
	return redirect('Status')




def EditBank(request, id):
	bank = Receivingbankpawnshop.objects.get(id=id)
	context = {'bank':bank}
	return render(request, 'editbank.html', context)


def UpdateBank(request, id):
	bank = Receivingbankpawnshop.objects.get(id=id)
	bank.bank_pawnshop = request.POST['banks']
	bank.time = request.POST['banktime']
	bank.date = request.POST['bankdate']
	bank.save()
	return redirect('Status')

def DeleteBank(request, id):
	bank = Receivingbankpawnshop.objects.get(id=id)
	bank.delete()
	return redirect('Status')







def EditInq(request, id):
	Inqs = Inquries.objects.get(id=id)
	context = {'Inqs':Inqs}
	return render(request, 'editinq.html', context)


def UpdateInq(request, id):
	Inqs = Inquries.objects.get(id=id)
	Inqs.iname = request.POST['nameinquiries']
	Inqs.typemessage = request.POST['contactinquiries']
	Inqs.comments = request.POST['typemessage']
	Inqs.rate = request.POST['rate']

	Inqs.save()
	return redirect('Inquiries')

def DeleteInq(request, id):
	Inqs = Inquries.objects.get(id=id)
	Inqs.delete()
	return redirect('Inquiries')


# def manipulationofdata():

# 	pname = Psrsignup(completename="Rabiya Mateo", address="Iloilo City", occupationhead="Advocate", salaryhead="15 000")
# 	pname.save()

# 	#readall
# 	objects = pendingname.objects.all()
# 	rslt = 'Printing all entries in Psrsignup model : <br>'
# 	for x in objects:
# 		res+= x.completename+"<br"

# 	#readspecific
# 	pname = Psrsignup.objects.get(id="pname")
# 	res += 'Printing One entry <b>'
# 	res += pname.address

# 	#delete
# 	res += '<br>Deleting an entry<br>'
# 	pname.delete()

# 	#update




# # def Assistance(request):
# # 	return render(request,'additionalassistance.html')

# # def Assistanceget(request):
# # 	assist = Additionalassistance.objects.create(
# 		aaname = request.POST['appname'],
# 		aaaddress = request.POST['appaddress'],
# 		contact = request.POST['appcontact'],
# 		loan = request.POST['apploan'],

# 		)
# 	return redirect('Assisting')
# 	return render(request, 'additionalassistance.html')

# def Assisting(request):

# 	assist = Additionalassistance.objects.all()

# 	return render(request,'additionalassistance.html', {'assist': assist})

# def New(request):
# 	pname = Psrsignup.objects.create(
# 		firstname =request.POST['firstname'],
# 		lastname = request.POST['surname'],
# 		address = request.POST['address'],
# 		salaryhead = request.POST['salary'],
# 		occupationhead = request.POST['occupation'],

# 		)

# 	return redirect(f'/prac/{pname.id}/')

# 	inquire = Inquiries.objects.create(
# 			inquire = inquire, 
# 			iname=request.POST['nameinquiries'], 
# 			icontact=request.POST['contactinquiries'], 
# 			rate=request.POST['typemessage'],
# 			comments=request.POST['message'],
# 			)

# 	return redirect(f'/prac/{inquire.id}/')

# def addinquire(request, inquirie):
# 		inquire = Inquiries.objects.get(id=inquire)
# 		return redirect(f'/prac/{inquire.id}/')

# def viewinquire(request, inquire):

# 		inquire = Inquires.objects.get(id=inquire)
# 		return render(request, 'inquiresandcomments.html', {'inquire': inquire, 'iname':'nameinquiries',
# 			'icontact':'contactinquiries',
# 			'rate': 'typemessage',
# 			'comments':'message',
# 			})








# def addItem(request, pn):
# 	pn = Psrsignup.objects.get(id=pn)
# 	Item.objects.create(pname=pn,text=request.POST['surname'], address=request.POST['address'])


# 	return redirect(f'/prac/{pn.id}/')






























# def Main(request):
# 	# firstdata = pendingname.objects.create()
# 	return render(request, 'psrform.html')
# def View(request, pname):
# 	pn = pendingname.objects.get(id=pname)
# 	return render(request, 'psrlist.html', {'pn': pn, 'address': 'address'}) #PINALTAN KO RIN PANG TRY LANG

# def New(request):
# 	newName = pendingname.objects.create()
# 	Item.objects.create(pname=newName, text=request.POST['surname'], address=request.POST['address'])
# 	return redirect(f'/prac/{newName.id}/') #variablename

# 	# money = income.objects.create()
# 	# Money.objects.create(mney=money, occu=request.POST['occu'], salary=request.POST['salary'])
# 	# return redirect(f'/prac/{money.id}/')

# def addItem(request, pname):
# 	pn = pendingname.objects.get(id=pname)
# 	Item.objects.create(pname=pn, text=request.POST['surname'], address=request.POST['address'])
# 	return redirect(f'/prac/{pn.id}/')

# 	# my = income.objects.get(id=mney)
# 	# Money.objects.create(mney=my, occu=request.POST['occu'], salary=request.POST['salary'])
# 	# return redirect (f'/prac/{my.id}/')



# def manipulationofdata():


#1

	# my = income.objects.get(id=mney)




#3

	#	# money = income.objects.create()
	# Money.objects.create(mney=money, occu=request.POST['occu'], salary=request.POST['salary'])
	# return redirect(f'/prac/{money.id}/')



#4
	# my = income.objects.get(id=mney)
	# Money.objects.create(mney=my, occu=request.POST['occu'], salary=request.POST['salary'])
	# return redirect (f'/prac/{my.id}/')










# address=request.POST['address'])

	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['surname'])
	# 	return redirect('/psr/viewlist_url/')

	# return render(request, 'psrform.html', {'sname' : items})


	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['surname'])
	# 	return redirect('/psrform/viewlist_url')




	#return render(request,'psrform.html')

#def Main(request):
	# 	if request.method == 'POST':
	# 	newIt = request.POST['surname']
	# 	Item.objects.create(text=newIt)
	# else:
	# 	newIt = ''
	# return render(request,'psrform.html',{'sname' : newIt,})

	# item1 = Item()
	# item1.text=request.POST.get('surname', '')
	# return render(request,'psrform.html',{'sname': item1.text ,})


	# item1.save()
	# item2 = Item()
	# item2.text=request.POST.get('givenname', '')
	# item2.save()

	#return render(request,'psrform.html',{'sname':request.POST.get('surname') ,'gname': request.POST.get('givenname',''),})

"""def Main(request):
	if request.method == 'POST':
		return HttpResponse(request.POST['surname'])
	return render(request,"psrform.html")

	def Main(request):
	return render(request,'psrform.html',{'sname':request.POST.get('surname') ,'gname': request.POST.get('givenname',''),})"""

 
# Create your views here.
