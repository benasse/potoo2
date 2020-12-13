from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from jinja2 import Template

def index(request):
    return HttpResponse("Please set the gatewayconfig_id in the url")


def generate_config(request,gatewayconfig_id):
    config =  GatewayConfig.objects.get(pk=gatewayconfig_id)
    substitute =  config.__dict__
    substitute['template_name'] = config.template.__dict__['name']
    substitute['template_file'] = config.template.__dict__['file']
    with open(str(config.template.file), 'r') as t:
        template = Template(t.read())
    output = template.render(substitute)
    output_name = '-'.join([substitute['name'],substitute['gateway_ip'],substitute['template_name']])
    response =  HttpResponse(output, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(output_name)
    return response
