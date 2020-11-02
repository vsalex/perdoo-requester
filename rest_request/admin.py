from django.contrib import admin
from .models import RESTRequest, RESTResponse 


@admin.register(RESTRequest)
class RESTRequestAdmin(admin.ModelAdmin):
    readonly_fields = ('completed',)


@admin.register(RESTResponse)
class RESTResponseAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
