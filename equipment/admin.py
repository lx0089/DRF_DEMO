from django.contrib import admin
from equipment.models import Pc, Server, NetworkEquipment

# Register your models here.

admin.site.register(Pc)
admin.site.register(Server)
admin.site.register(NetworkEquipment)
