from django.db import models
from django.utils import timezone


class Psrsignup(models.Model):
	completename = models.CharField(max_length=50, default="", null=True)
	address = models.TextField(default="")
	occupationhead = models.CharField(max_length=50, default="")
	salaryhead = models.IntegerField(default="")

class Familyinfo(models.Model):
	completename = models.ForeignKey(Psrsignup, null=True, on_delete=models.CASCADE)
	familyname1 = models.CharField(max_length=50, default="")
	familyname2 = models.CharField(max_length=50, default="")
	familyname3 = models.CharField(max_length=50, default="")
	occupation1 = models.CharField(max_length=50, default="")
	occupation2 = models.CharField(max_length=50, default="")
	occupation3 = models.CharField(max_length=50, default="")
	salary1 = models.IntegerField(default="")
	salary2 = models.IntegerField(default="")
	salary3 = models.IntegerField(default="")
	totalsalary = models.IntegerField(default="")

class Subsidyconfirmation(models.Model):
	completename = models.ForeignKey(Psrsignup, null=True, on_delete= models.CASCADE)
	file = models.FileField(blank=True, null=True)
	contact = models.IntegerField(default="")
	date = models.DateTimeField(auto_now_add=True)
	subsidy = models.IntegerField(default="")

class Receivingplacedate(models.Model):
	completename = models.ForeignKey(Psrsignup, null=True, on_delete= models.CASCADE)

	PLACE_CHOICES = (
	    ('Phase 1', 'PHASE1'),
	    ('Phase 2', 'PHASE2'),
	    ('Phase 3', 'PHASE3'),
	    ('Phase 4', 'PHASE 4'),
	)
	place = models.CharField(max_length=50, default="", choices=PLACE_CHOICES, null=True)
	date = models.DateField(default="")
	time = models.TimeField(default="")

class Receivingbankpawnshop(models.Model):
	completename = models.ForeignKey(Psrsignup, null=True, on_delete= models.CASCADE)
	BANKPAWN_CHOICES = (
	    ('Landbank', 'LANDBANK'),
	    ('PNB', 'PNB'),
	    ('MLHUILLER', 'MLHUILLER'),
	    ('PALAWAN', 'PALAWAN'),
	)

	bank_pawnshop = models.CharField(max_length=50, default="", choices=BANKPAWN_CHOICES, null=True)
	date = models.DateField(default="")
	time = models.TimeField(default="")

class Inquries(models.Model):
	iname = models.CharField(max_length=30, default="")
	icontact = models.IntegerField(default=None)
	comments = models.TextField(default="")
	RATE_CHOICES = {
		('poor', 'poor'),
		('weak', 'weak'),
		('good', 'good'),
		('very good', 'very good'),
		('excellent', 'excellent'),
	}
	rate = models.CharField(max_length=15, default="", choices =RATE_CHOICES, null=True)
	TYPE_CHOICES = {
	('Suggestion', 'Suggestion'),
	('Question', 'Question'),
	('Comment', 'Comment'),
	}

	typemessage = models.CharField(max_length=15, default="", choices = TYPE_CHOICES, null=True)



	

