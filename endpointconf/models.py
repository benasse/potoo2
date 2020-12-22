from django.db import models

# Create your models here

class Template(models.Model):
    name = models.CharField(max_length=200, help_text='The name of your template')
    file = models.FileField(upload_to='endpoint-templates/', help_text='The name of your template')
    max_line_number = models.IntegerField()

    def file_link(self):
        if self.file:
            return "<a href='%s'>download</a>" % (self.file.url,)
        else:
            return "No attachment"

        file_link.allow_tags = True


    def __str__(self):
        return self.name + ' - ' + str(self.file)

class EndpointConfig(models.Model):
    name = models.CharField(max_length=200, help_text='The name of the endpoint config')

    ipbx_ip = models.GenericIPAddressField(help_text='The IP address of the IPBX on witch your endpoint will register')

    gateway_ip = models.GenericIPAddressField(help_text='The IP adress of the endpoint')
    gateway_mask = models.GenericIPAddressField(default='255.255.255.0', help_text='The netmask of the endpoint')
    gateway_gw = models.GenericIPAddressField(null=True,blank=True,default='', help_text='The defaut gateway of the endpoint')
    gateway_password = models.CharField(max_length=200, blank=True, help_text='The admin password of the endpoint')
    gateway_ntp = models.GenericIPAddressField(null=True,blank=True,default='', help_text='The ntp server used by the endpoint')
    gateway_dns1 = models.GenericIPAddressField(null=True,blank=True,default='', help_text='The dns serveur used by the endpoint')

    TONE = [
      ('FR','FR')
    ]

    tone = models.CharField(max_length=2, choices=TONE)
    template = models.ForeignKey(Template, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name + ' - ' + self.gateway_ip


class LineConfig(models.Model):
    description = models.CharField(max_length=200, help_text='Some information about the line')
    ipbx_auth_username = models.CharField(max_length=200, help_text='The SIP username used to register on the IPBX')
    ipbx_auth_password = models.CharField(max_length=200, help_text='The SIP password used to register on the IPBX')
    template = models.ForeignKey(EndpointConfig, on_delete=models.CASCADE)
