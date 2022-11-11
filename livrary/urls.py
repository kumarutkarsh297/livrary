from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "LIVRARY | Admin Portal"
# admin.site.site_title = "LIVRARY | Admin Portal"
admin.site.index_title = "LIVRARY | Administration Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls'))
]
