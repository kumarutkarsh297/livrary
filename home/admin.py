from django.contrib import admin
from home.models import Books
from home.models import Members
from home.models import Rates
from home.models import Issued

# Register your models here.
admin.site.register(Books)
admin.site.register(Members)
admin.site.register(Rates)
admin.site.register(Issued)