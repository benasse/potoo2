from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

from jinja2 import Template

def index(request):
    return HttpResponse("Please set the gatewayconfig_id in the url")

def generate_config(request,gatewayconfig_id):
    config =  GatewayConfig.objects.get(pk=gatewayconfig_id)
    params =  config.__dict__
    params['template_name'] = config.template.__dict__['name']
    params['template_file'] = config.template.__dict__['file']
    params['created_date'] = datetime.now()
    with open(str(config.template.file), 'r') as t:
        template = Template(t.read())
    output = template.render(params)
    output_name = '-'.join([params['name'],params['gateway_ip'],params['template_name']])
    response =  HttpResponse(output, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(output_name)
    return response
