# this view is before using mixins for Permissions

from rest_framework import generics, mixins, permissions, authentication

from ..api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializers
from .models import Product
from api.authentication import TokenAuthentication

from rest_framework.decorators import api_view
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers

  def perform_create(self, serializer):
    print("Inside the serializer")
    print(serializer.validated_data)
    print("End")
    serializer.save() # You can send a Django Signals

product_create_api_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  # lookup_field = 'pk'
  permission_classes = [permissions.DjangoModelPermissions]

  
product_detail_api_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  lookup_field = 'pk'

  def perform_create(self, serializer):
    serializer.save()
  
product_update_api_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  lookup_field = 'pk'

  def perform_destroy(self, instance):
    super().perform_destroy(instance)
  
product_delete_api_view = ProductDeleteAPIView.as_view()

# Either use ListAPIView or ListCreateAPIView

class ProductListAPIView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  # lookup_field = 'pk'
  
product_list_api_view = ProductDetailAPIView.as_view()

# ListCreateAPIView i.e., CreateAPIView and ListAPIView views are integrated into one.

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
  authentication_classes = [authentication.SessionAuthentication, TokenAuthentication] # Here's we've used api.authenticaiton which is our own custom auth token that we created to use the keyword "Bearer" while defining the token auth in the py_client.list.py
  permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

  def perform_create(self, serializer):
    print("Inside the serializer")
    print(serializer.validated_data)
    print("End")
    serializer.save() # You can send a Django Signals

product_list_create_api_view = ProductListCreateAPIView.as_view()

class ProductMixinView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  lookup_field = 'pk'
  
  # In class based views, we need to create a function by ourselves saying get() or post()
  def get(self, request, *args, **kwargs):
    pk = kwargs
    print(args, kwargs)
    if pk is not None:
      return self.retrieve(request, *args, **kwargs)
    return self.list(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()

# Below is the view function way to make the ListCreate generics. 
# Basically, you can now use GET method to see all (or select) products
# You can also use the POST method to put inside a value in the database 

@api_view(['POST', 'GET'])
def product_alt_view(request, pk=None, *args, **kwargs):
  method = request.method

  if method == 'GET':
    if pk is not None:
      obj = get_object_or_404(Product, pk=pk)
      data = ProductSerializers(obj , many=False).data
      return Response(data)
    queryset = Product.objects.all()
    data = ProductSerializers(queryset, many=True).data
    return Response(data)
  
  elif method == 'POST':
    serializer = ProductSerializers(data = request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data.get('Title')
      serializer.save()
      return Response(serializer.data)
    else:
      return Response({"invalid":"not good data."}, status=400)