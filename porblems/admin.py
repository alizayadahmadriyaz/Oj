from django.contrib import admin
from porblems.models import problemm,solution,Test_Case
# Register your models here.
admin.site.register([problemm])
admin.site.register([solution])
admin.site.register([Test_Case])