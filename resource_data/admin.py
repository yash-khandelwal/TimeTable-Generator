from django.contrib import admin
from resource_data import models
# Register your models here.
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['teacher_code','first_name','last_name','department']

class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_code', 'branch_name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_code', 'branch_code', 'sem',
                    'credits','lecture','tutorial','practical','course_intro']

admin.site.register(models.Branch, BranchAdmin)
admin.site.register(models.Teacher,TeachersAdmin)
admin.site.register(models.Course,CourseAdmin)
admin.site.register(models.Room)
