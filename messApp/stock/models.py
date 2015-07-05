# encoding: utf-8
import datetime

from django.db import models
from django.utils import timezone
#from users.models import User, UserDetails 
#can use models of other app to create a project

# Create your models here.
class Item(models.Model):
	item_id=models.CharField(max_length=10,primary_key=True) #db_column , The name of the database column to use for this field
	item_name=models.CharField(max_length=30)	#change the primary key to  name
	item_unit=models.CharField(max_length=10)#shorthand
	quantity=models.IntegerField(default=0)
	balance=models.IntegerField(default=0)
	timestamp=models.DateTimeField('date recently modified',auto_now=True)
	#use an optional first positional argument to a Field to designate a human-readable name 

	def __unicode__(self): 
		return u'%s' % (self.item_name) #objects representations

	class Meta:
		ordering=['item_id','item_name']

"""
check unit table and relationship
"""
class Unit(models.Model):
	name=models.OneToOneField(Item,primary_key=True,related_name='Unit')#shorthand
	fullname=models.CharField(max_length=10)
	#check if the relation should be with this variable? or convert this to full name

	def __unicode__(self):
		return u'%s' % (self.fullname)


class Transaction(models.Model):
	TRANSACTION_TYPE = (
        ('Consumption', 'Consumption'),
        ('Purchase', 'Purchase'),
        ('Expired', 'Expired'),
    )
	item=models.ForeignKey(Item,related_name='Transaction')	#foreign key to primary key of item ,@todo -> set it to name item 
	#to_field='item_name', in above relationship
	transaction_type=models.CharField(max_length=11,choices=TRANSACTION_TYPE)	#default=FRESHMAN
	quantity=models.IntegerField(default=0)
	cost=models.IntegerField(default=0)
	inventory=models.IntegerField(default=0)
	date=models.DateField('Date issued',auto_now_add=True)	#Automatically set the field to now when the object is first created
	timestamp=models.DateTimeField('Transaction date',auto_now=True)#Automatically set the field to now every time the object is saved/edited
	consumption=models.IntegerField(default=0)
	comments=models.CharField(max_length=50)

	def was_transacted_recently(self):# a custom method,
		return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
	was_transacted_recently.admin_order_field = 'timestamp'
	was_transacted_recently.boolean = True
	was_transacted_recently.short_description = 'transacted recently?'

	def __unicode__(self):
		return u'%s : %s : %s' % (self.transaction_type,self.cost,self.timestamp)
	"""
	To order by pub_date descending, then by author ascending,
	ordering = ['-pub_date', 'author']
	"""	
	class Meta:
		ordering=['item','-timestamp']
		#unique_together = ('field1', 'field2',)

"""
custom save method , overloading save() , check 
http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
"""
	# def save(self, *args, **kwargs):
 #        ''' On save, update timestamps '''
 #        if not self.id:
 #            self.created = datetime.datetime.today()
 #        self.modified = datetime.datetime.today()
 #        return super(User, self).save(*args, **kwargs)