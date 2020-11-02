from django.contrib import admin
from .models import RESTRequest, RESTResponse 


class RESTResponseInline(admin.StackedInline):
    model = RESTResponse
    can_delete = False
    readonly_fields = ('headers', 'status_code', 'data')


@admin.register(RESTRequest)
class RESTRequestAdmin(admin.ModelAdmin):
    readonly_fields = ('completed',)
    list_display = ('id', 'url', 'method', 'started', 'completed', 'user')
    inlines = (
        RESTResponseInline,
    )


@admin.register(RESTResponse)
class RESTResponseAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        # Disable delete:
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions
