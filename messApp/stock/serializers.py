from rest_framework import serializers
from stock.models import Item,Unit,Transaction

#ModelSerializer classes are simply a shortcut for creating serializer classes
#with Simple default implementations for the create() and update() methods.
class UnitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Unit
		fields = ('name', 'fullname')

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction


class ItemSerializer(serializers.ModelSerializer):
	Unit = serializers.RelatedField(many=False)
	#RelatedField is used to represent the target of the relationship using its __unicode__ method
	Transaction = serializers.RelatedField(many=True)
	# check 	HyperlinkedRelatedField is used to represent the target of the relationship using a hyperlink
		
	class Meta:
		model = Item
		fields=('item_id','item_name','item_unit','quantity','balance','timestamp','Unit','Transaction')
		


				



					
