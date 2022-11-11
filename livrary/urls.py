from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "LIVRARY Admin"
admin.site.site_title = "LIVRARY Admin Portal"
admin.site.index_title = "Welcome to LIVRARY Admin Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls'))
]
