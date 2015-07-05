from stock.models import Item,Unit,Transaction
from stock.serializers import ItemSerializer,UnitSerializer,TransactionSerializer
#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import Http404   #lives in the django.http module
from django.template import RequestContext,loader
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication  ?? check
# below line for user privilege
# from django.contrib.auth.models import User


# these are generic views
# Create your views here.


# class ItemList(APIView):
#     """
#     List all items, or create a new item.
#     """
#     # authentication_classes = (JSONWebTokenAuthentication,)
#     def get(self, request, format=None):
#         item = Item.objects.all() #here  Item is the model
#         serializer = ItemSerializer(item, many=True)
#         return Response(serializer.data)


#     def post(self, request, format=None):
#         serializer=ItemSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		

"""
class based views , implementing DRY principle
@todo set permission classes !
"""
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an item instance.
    """
    model = Item
    serializer_class = ItemSerializer
    # allowed_methods = ['get', 'post', 'put', 'delete', 'options']
    
    # def options(self, request, id):
    #     response = HttpResponse()
    #     response['allow'] = ','.join([allowed_methods])
    #     return response

    # def get(self, request, pk, format=None):
    #     item = Item.objects.get(item_id=pk)    #filter if many returns , return exception if no value or use get_object custom method
    #     serializer = ItemSerializer(item)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer=ItemSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk, format=None):
    #     item = self.get_object(pk)
    #     serializer = ItemSerializer(item, data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


# class TransactionList(APIView):
#     """
#     List all Transactions, or create a new Transaction.
#     """
#     # authentication_classes = (JSONWebTokenAuthentication,)
#     def get(self, request, format=None):
#         transaction = Transaction.objects.all() 
#         serializer = TransactionSerializer(transaction, many=True)
#         return Response(serializer.data)


#     def post(self, request, format=None):
#         serializer=TransactionSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		


# class TransactionDetail(APIView):
#     """
#     Retrieve, update or delete a Transaction instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Transaction.objects.get(pk=pk)
#         except Transaction.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         transaction = self.get_object(pk)
#         serializer = TransactionSerializer(transaction)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         transaction = self.get_object(pk)
#         serializer = TransactionSerializer(transaction, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         transaction = self.get_object(pk)
#         transaction.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



"""
using generic class based views
"""


class ItemList(generics.ListCreateAPIView):
    """
    List all items, or create a new item.
    """
    model = Item
    serializer_class = ItemSerializer
    #The serializer and queryset will be automatically generated for you.

    # def get(self, request, pk, format=None):
    #     item = Item.objects.get(item_id=pk)    #filter if many returns , return exception if no value
    #     serializer = ItemSerializer(item)
    #     return Response(serializer.data)
    
    # allowed_methods = ['get', 'post', 'put', 'delete', 'options']
    
    # def options(self, request, id):
    #     response = HttpResponse()
    #     response['allow'] = ','.join([allowed_methods])
    #     return response

    # def post(self, request, format=None):
    #     serializer=ItemSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    		


# class ItemDetail(generics.ListCreateAPIView):
#     """
#     Retrieve, update or delete a item instance.
#     """
#     model = Item
#     serializer_class = ItemSerializer
    


# class TransactionList(generics.ListCreateAPIView):
#     """
#     List all Transactions, or create a new Transaction.
#     """
#     model = Transaction
#     serializer_class = TransactionSerializer
    	


# class TransactionDetail(generics.RetrieveUpdateDestroyAPIView): 
#     """
#     Retrieve, update or delete a Transaction instance.
#     """
#     model = Transaction
#     serializer_class = TransactionSerializer

#ReadOnlyModelViewSet  : for read only operations
#ModelViewSet          : complete set of default read and write operations
#to bind viewset to url , create views from viewset in urls.py
#viewset are resources / controller 
class TransactionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

"""
view function
param: request 
(object that has info about the request that has trigered the view)
an instance of the class django.http.HttpRequest
"""
def index(request):
    latest_items=Item.objects.all().order_by('timestamp')[:2]
    # output=', '.join([p.item_name for p in latest_items])
    # return HttpResponse(output)
    """
    template = loader.get_template('StockAPI/index.html')
    context = RequestContext(request, {
        'latest_items': latest_items,
    })
    return HttpResponse(template.render(context))
    """
    #a shortcut render
    # context = {'latest_items': latest_items}
    # return render(request, 'StockAPI/index.html', context)    #create template
    return HttpResponse("Hi!!")

def detail(request,item_id):
    item=get_object_or_404(Item,pk=item_id)
    return render(request,'StockAPI/detail.html',{'item':item})