from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("market/", admin.site.urls),
    path("chatting/", admin.site.urls),
    path("insta/", admin.site.urls),
    path("accounts/", admin.site.urls),
]