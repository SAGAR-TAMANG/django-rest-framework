import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
  body = request.body # Byte string of JSON data
  data = {}
  try:
    data = json.loads(body) # String of JSON -> Python Dict 
  except Exception as e:
    pass
  data['headers'] = request.headers
  data['content_type'] = request.content_type
  json.dumps(request.headers)
  print(data)
  return JsonResponse({"message":"Hi there! This is your Django API response."})