import json
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializers

@api_view(["GET", "POST"])
def api_home(request, *args, **kwards):
  """"
  DRF API VIEW
  """
  instance = Product.objects.all().order_by("?").first()
  data = {}
  if instance:
    # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    data = ProductSerializers(instance).data
  
  return Response(data)