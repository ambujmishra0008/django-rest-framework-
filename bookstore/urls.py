
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome")


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('book/', include("book.url"))
]
