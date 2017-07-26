# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Clientes
from .models import Sitios
from .models import Claves
from .models import FrecuenciaRastreos
from .models import Tareas

admin.site.register(Clientes)
admin.site.register(Sitios)
admin.site.register(Claves)
admin.site.register(FrecuenciaRastreos)
admin.site.register(Tareas)
