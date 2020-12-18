from django.db import models

# Create your models here

class Template(models.Model):
    name = models.CharField(max_length=200, help_text='The name of your template')
    file = models.FileField(upload_to='gateway-templates/', help_text='The name of your template')

    def file_link(self):
        if self.file:
            return "<a href='%s'>download</a>" % (self.file.url,)
        else:
            return "No attachment"

        file_link.allow_tags = True


    def __str__(self):
        return self.name + ' - ' + str(self.file)

class GatewayConfig(models.Model):
    name = models.CharField(max_length=200, help_text='The name of your gateway config')

    ipbx_ip = models.GenericIPAddressField(help_text='The IP address of the IPBX on witch your gateway will register')
    ipbx_auth_username = models.CharField(max_length=200, help_text='The SIP username used to register on the IPBX')
    ipbx_auth_password = models.CharField(max_length=200, help_text='The SIP password used to register on the IPBX')

    gateway_ip = models.GenericIPAddressField(help_text='The IP adress of your gateway')
    gateway_mask = models.GenericIPAddressField(default='255.255.255.0', help_text='The netmask of your gateway')
    gateway_gw = models.GenericIPAddressField(null=True,blank=True,default='', help_text='The defaut gateway of your gateway')
    gateway_password = models.CharField(max_length=200, blank=True, help_text='The admin password of the gateway')
    gateway_ntp = models.GenericIPAddressField(null=True,blank=True,default='', help_text='The ntp server used by the gateway')
    gateway_dns1 = models.GenericIPAddressField(null=True,blank=True,default='', help_text='The dns serveur used by the gateway')

    TONE = [
      ('FR','FR')
    ]

    tone = models.CharField(max_length=2, choices=TONE)
    template = models.ForeignKey(Template, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name + ' - ' + self.gateway_ip
