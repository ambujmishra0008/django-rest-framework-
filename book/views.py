from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from django.http import JsonResponse
from rest_framework import decorators
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@decorators.api_view(http_method_names=["post"])
def booklist(req):
    # obj = Book.objects.get(id=1)
    # ser = BookSerializer(instance=obj)
    # print(ser.data)
    # return JsonResponse(ser.data)

    # json_data =  {'id': 1, 'title': 'Hindi', 'desc': 'This is my Hindi book', 'author':1}
    req_data = req.data
    dser = BookSerializer(data = req_data, many = True)
    print(dser.is_valid(raise_exception=True))
    print(dser.validated_data)
    dser.save()
    return JsonResponse({"okay":"success"})
    




















