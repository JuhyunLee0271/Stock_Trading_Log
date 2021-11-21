# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

# Admin 페이지에서 커스터마이징 한 User Model을 보여줄 관리 페이지
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name', 'nickname', 'email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('name', 'nickname', 'email', 'password')}),
        ("Personal info", {'fields': ('phone_number',)}),
        ("Permissions", {'fields': ('is_admin',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('name', 'nickname', 'email', 'phone_number', 'password1', 'password2'),
        })
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)