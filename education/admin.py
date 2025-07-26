from django.contrib import admin

from education.models import education

class EduAdmin(admin.ModelAdmin):
    list_display = ('Edu_date','Edu_title','Edu_Desc')
     

admin.site.register(education,EduAdmin)
# Register your models here.
