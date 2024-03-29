import json
from django.http import JsonResponse, HttpResponse

# Basics w/o Modles

# def api_home(request, *args, **kwargs):
#   print("GET REQUEST:", request.GET) # URL query params
#   print("GET REQUEST:", request.POST) # URL query params
  
#   body = request.body # Byte string of JSON data
#   data = {}
#   try:
#     data = json.loads(body) # String of JSON -> Python Dict 
#   except Exception as e:
#     pass
#   data['params'] = dict(request.GET)
#   data['headers'] = dict(request.headers)
#   data['content_type'] = request.content_type
#   print(data)
#   return JsonResponse({"message":"Hi there! This is your Django API response."})

# With Models

from products.models import Product
from django.forms.models import model_to_dict

def api_home(request, *args, **kwards):
  model_data = Product.objects.all().order_by("?").first()
  data = {}
  # if model_data:
  #   data['id'] = model_data.id
  #   data['title'] = model_data.title
  #   data['content'] = model_data.content
  #   data['price'] = model_data.price

  # if model_data:
  #   data = model_to_dict(model_data, fields=['id', 'title', 'price'])
  #   json_data_str = json.dumps(data)
  
  # return HttpResponse(json_data_str, headers={"content-type":"application/json"})

  if model_data:
    data = model_to_dict(model_data, fields=['id', 'title', 'price'])
  
  return JsonResponse(data)