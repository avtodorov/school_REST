from django.contrib import admin
from school_app.models import Student, Group

# Register your models here.

admin.site.register(Student)


class GroupAdmin(admin.ModelAdmin):
    raw_id_fields = ['students']


admin.site.register(Group, GroupAdmin)
