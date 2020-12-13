from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class GatewayConfigAdmin(admin.ModelAdmin):
    readonly_fields = ('gateway_config_link', )
    @mark_safe
    def gateway_config_link(self, gateway_config):
        url = '/gwconf/'
        return '<a href="{url}{id}">{url}{id}</a>'.format(
            url=url, 
            id=gateway_config.id
    )

    gateway_config_link.short_description = "Download Config"

    list_display = ('__str__','gateway_config_link')

admin.site.register(GatewayConfig,GatewayConfigAdmin)
admin.site.register(Template)
