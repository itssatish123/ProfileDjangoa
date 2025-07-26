from django.contrib import admin

from enqData.models import EnqData

# Register your models here.
class EnqAdmin(admin.ModelAdmin):
    list = ('nameFirst','mail','messageData')


admin.site.register( EnqData ,EnqAdmin)