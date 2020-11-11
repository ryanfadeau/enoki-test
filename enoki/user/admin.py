from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from user.models import User
class MyUserAdmin(UserAdmin):
    list_display = ("email", "username", "last_name", "first_name","date_joined", "last_login", "is_staff", )
    search_fields = ("email", "username", "is_staff")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, MyUserAdmin)
