from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from accounts.models import User, Batch, Result
# Register your models here.
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_locked', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

class BatchAdmin(admin.ModelAdmin):
    list_display = ['branch_sem','course_code','teacher_code','room','no_class_week','no_of_slots','course_schema']

class ResultAdmin(admin.ModelAdmin):
    list_display = ['cse3','cse5','ece3','ece5','it3','it5']

admin.site.register(User, MyUserAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Result, ResultAdmin)
