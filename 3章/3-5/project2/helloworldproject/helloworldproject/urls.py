from django.contrib import admin
from django.urls import path
from .views import helloworldfunc

urlpatterns = [
    path('admin/', admin.site.urls), #一時的に「admin/」を「hello/」に変更する
    path('helloworldurl/', helloworldfunc), 
]
