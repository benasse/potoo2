# Generated by Django 3.1.4 on 2020-12-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwconf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatewayconfig',
            name='gateway_dns1',
            field=models.GenericIPAddressField(blank=True, default='', help_text='The dns serveur used by the gateway', null=True),
        ),
        migrations.AddField(
            model_name='gatewayconfig',
            name='gateway_ntp',
            field=models.GenericIPAddressField(blank=True, default='', help_text='The ntp server used by the gateway', null=True),
        ),
        migrations.AlterField(
            model_name='gatewayconfig',
            name='tone',
            field=models.CharField(choices=[('FR', 'FR')], max_length=2),
        ),
    ]
