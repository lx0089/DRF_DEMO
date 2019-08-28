# Generated by Django 2.2.3 on 2019-08-28 03:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipment', '0002_server_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eq_type', models.CharField(choices=[(1, '路由器'), (2, '交换机'), (3, '其他设备')], max_length=16, verbose_name='设备类型')),
                ('eq_ip', models.CharField(max_length=32, unique=True, verbose_name='设备IP')),
                ('eq_brand', models.CharField(blank=True, max_length=32, null=True, verbose_name='设备品牌')),
                ('eq_username', models.CharField(blank=True, max_length=16, null=True, verbose_name='设备登录名')),
                ('eq_password', models.CharField(blank=True, max_length=32, null=True, verbose_name='设备登录密码')),
                ('eq_location', models.CharField(blank=True, max_length=32, null=True, verbose_name='位置')),
                ('eq_wifiname', models.CharField(blank=True, max_length=32, null=True, verbose_name='WIFI名')),
                ('eq_wifipwd', models.CharField(blank=True, max_length=32, null=True, verbose_name='WIFI密码')),
                ('eq_theuser', models.CharField(blank=True, max_length=32, null=True, verbose_name='使用者')),
                ('eq_broadbandname', models.CharField(blank=True, max_length=16, null=True, verbose_name='宽带拨号名')),
                ('eq_broadbandpwd', models.CharField(blank=True, max_length=16, null=True, verbose_name='宽带拨号密码')),
                ('eq_mobile', models.CharField(blank=True, max_length=16, null=True, verbose_name='绑定电话')),
                ('eq_note', models.CharField(blank=True, max_length=32, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '网络设备',
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='NetworkTopology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='img/network/', verbose_name='拓扑图')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '拓扑图',
                'verbose_name_plural': '拓扑图',
            },
        ),
        migrations.AddField(
            model_name='pc',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pcs', to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
    ]
