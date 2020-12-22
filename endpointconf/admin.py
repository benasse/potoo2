from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe



class LineConfigInline(admin.StackedInline):
      model = LineConfig
#      extra = 3

class EndpointConfigAdmin(admin.ModelAdmin):
#    readonly_fields = ('endpoint_config_link', )
#    @mark_safe
#    def gateway_config_link(self, gateway_config):
#        url = '/endpointconf/'
#        return '<a href="{url}{id}">{url}{id}</a>'.format(
#            url=url, 
#            id=gateway_config.id
#    )
#
#    gateway_config_link.short_description = "Download Config"
#
#    list_display = ('__str__','gateway_config_link')
    inlines = [LineConfigInline]

admin.site.register(EndpointConfig,EndpointConfigAdmin)
#admin.site.register(LineConfig)
admin.site.register(Template)
