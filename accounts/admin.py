from django.contrib import admin
from .models import User
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'username','phone_number', 'date_joined', 'last_login', 'is_staff', 'is_superuser', 'is_active', 'auth_provider')
#     search_fields = ('email', 'username')
#     list_filter = ('is_staff', 'is_superuser', 'is_active')
# admin.site.register(User, UserAdmin)
from django.contrib import admin
from .models import User,OTP,WishList
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'username','first_name','last_name', 'date_joined', 'last_login', 'is_staff', 'is_superuser', 'is_active','email','is_vendor','password'] 

admin.site.register(User, UserAdmin)
admin.site.register(OTP)
admin.site.register(WishList)
