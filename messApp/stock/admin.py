from django.contrib import admin
from stock.models import Item,Unit,Transaction

# Register your models here.
class UnitAdmin(admin.ModelAdmin):
	list_display = ('name','fullname')

class UnitInline(admin.StackedInline):
    model = Unit    

class ItemAdmin(admin.ModelAdmin):
	#to split the form up into fieldsets
    fieldsets = [
        ('Item Details',               {'fields': ['item_id','item_name','item_unit','quantity','balance']}),
        ('Date information', {'fields': ['timestamp']}),#fields tuples  well formed & a tuple with only one element
    ]
    list_display = ('item_name','item_unit', 'quantity','balance')#to  display more option in admin change list
    readonly_fields = ("timestamp",)
    inlines = [UnitInline]

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transaction Details',               {'fields': ['item','transaction_type','quantity','cost','inventory','date','consumption']}),
        ('Date information', {'fields': ['timestamp']}),
        ('Comments', {'fields': ['comments']}),
    ]
    list_display = ('item','quantity', 'inventory','timestamp')
    list_filter=['timestamp'] #date_hierarchy : another way 
    search_fields=['item'] #ordering 
    # filter_horizontal : check ! works on many to many fields
    # raw_id_fields : check!
    readonly_fields = ("date","timestamp")#no field to set time even by admin panel
    #The error is due to date having auto_now_add=True (or auto_now=True). As the value is automatic, it's not editable, so it's not in the form
    
#create a model admin object, then pass it as the second argument to admin.site.register() 
admin.site.register(Item,ItemAdmin)
admin.site.register(Unit,UnitAdmin)
admin.site.register(Transaction,TransactionAdmin)
