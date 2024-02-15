from django.contrib import admin
from .models import New_User
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display=('reg_no','name','email','phone','age')
admin.site.register(New_User,Admin)
