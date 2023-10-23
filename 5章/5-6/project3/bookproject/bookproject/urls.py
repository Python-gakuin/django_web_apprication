#3-5同様、上の文字は消去しても問題ありません。
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('book.urls')),
]
