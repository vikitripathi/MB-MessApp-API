from django.conf.urls import patterns, include, url
#from django.contrib import admin
# from django.views.generic import list_detail
from rest_framework.urlpatterns import format_suffix_patterns
from stock import views
from stock.models import Item 
from rest_framework.routers import DefaultRouter


"""
we're creating multiple views from each ViewSet class, by binding the http methods to the required action for each view.
"""
transaction_list=views.TransactionViewSet.as_view({
	'get': 'list',
    'post': 'create'
	})

transaction_detail=views.TransactionViewSet.as_view({
	'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
	})

# Item_List={
# 	'queryset':Item.objects.all(),
#     'template_name': 'item_list_page.html',
# }

"""
use router  instead of url conf
"""
# Create a router and register our viewsets with it.
# router=DefaultRouter()
# router.register(r'transaction',views.TransactionViewSet)
# router.register(r'item',views.ItemViewSet)
"""
check vamshi code , this url routing should be in main urls.py
"""

"""
loose coupling of url and view !
url dispatching/routing order is top to bottom  in the given list
^ start
$ end
\d any single digit
? zero or one of the previous expressions
+ one or more  of the prev expressions
* zero or more of
"""
#use named regular expression groups to capture URL bits and pass them as keyword arguments to a view
#(?P<param_name>)
#use () to capture it 
#prevent argument order bug
#(r'^mydata/birthday/$', views.my_view, {'month': 'jan', 'day': '06'}),  #pass extra param to make view  function generic
urlpatterns = patterns('',
url(r'^$', views.index,name='index'),	#r -> raw string (don't ignore backslashes)
url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
url(r'^item/$', views.ItemList.as_view()),
url(r'^item/(?P<pk>\d+)/$', views.ItemDetail.as_view()),#check regex in detail
#url(r'^transaction/$', views.TransactionList.as_view()),
url(r'^transaction/$', transaction_list,name='transaction-list'),		#use viewset
#url(r'^transaction/(?P<pk>\d+)/$', views.TransactionDetail.as_view()),
url(r'^transaction/(?P<pk>\d+)/$', transaction_detail,name='transaction-detail'),
#url(r'^itemlist/$',list_detail.object_list,Item_List),  #for template direct binding
)
urlpatterns = format_suffix_patterns(urlpatterns)

"""
check the django part of the tutorial
http://blog.kevinastone.com/getting-started-with-django-rest-framework-and-angularjs.html
"""