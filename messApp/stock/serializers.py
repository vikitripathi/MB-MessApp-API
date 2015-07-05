from rest_framework import serializers
from stock.models import Item,Unit,Transaction

#ModelSerializer classes are simply a shortcut for creating serializer classes
#with Simple default implementations for the create() and update() methods.
#When using the ModelSerializer class, serializer fields and relationships will be automatically generated for you
class UnitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Unit
		fields = ('name', 'fullname')

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		#depth = 1

"""
http://stackoverflow.com/questions/14573102/how-do-i-include-related-model-fields-using-django-rest-framework
check for creating nested serializers ,or nested json response
"""
class ItemSerializer(serializers.HyperlinkedModelSerializer):
	Unit = serializers.RelatedField(many=False)
	#RelatedField is used to represent the target of the relationship using its __unicode__ method
	#Transaction = serializers.RelatedField(many=True)	#many- for to many relationship type
	# Transaction =serializers.HyperlinkedRelatedField(
	# 	many=True,
	# 	read_only=True,
	# 	view_name='TransactionDetail.as_view()'
	# )
	Transaction=TransactionSerializer(many=True,read_only=True)	#to create nested json response 
	"""
	Transaction = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='transaction_type'
     )
	"""
	# check 	HyperlinkedRelatedField is used to represent the target of the relationship using a hyperlink
		
	class Meta:
		model = Item
		fields=('item_id','item_name','item_unit','quantity','balance','timestamp','Unit','Transaction')
		depth = 1
		


				



					
