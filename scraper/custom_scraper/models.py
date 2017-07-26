# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

class Clientes(models.Model):
    nombre = models.CharField(max_length=200, verbose_name=(u'nombre'))
    falta = models.DateTimeField(verbose_name=(u'fecha de alta'))
    fbaja = models.DateTimeField(blank=True, null=True, verbose_name=(u'fecha de baja'))

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name=(u'Cliente')
        verbose_name_plural=(u'Clientes')


class Sitios(models.Model):
    nombre = models.CharField(max_length=200, verbose_name=(u'nombre'))
    falta = models.DateTimeField(verbose_name=(u'fecha de ealta'))
    fbaja = models.DateTimeField(blank=True, null=True, verbose_name=(u'fecha de baja'))

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name=(u'Sitio')
        verbose_name_plural=(u'Sitios')

class Claves(models.Model):
    lista = models.TextField(verbose_name=(u'lista'))
    falta = models.DateTimeField(verbose_name=(u'fecha de alta'))
    fbaja = models.DateTimeField(blank=True, null=True, verbose_name=(u'fecha de baja'))

    def __str__(self):
        return self.lista

    class Meta:
        verbose_name=(u'Clave')
        verbose_name_plural=(u'Claves')

class FrecuenciaRastreos(models.Model):
    frecuencia = models.CharField(max_length=10, verbose_name=(u'frecuencia'))
    descripcion = models.CharField(max_length=200, verbose_name=(u'descripción'))
    falta = models.DateTimeField(verbose_name=(u'fecha de alta'))
    fbaja = models.DateTimeField(blank=True, null=True, verbose_name=(u'fecha de baja'))

    def __str__(self):
        return self.descripcion.encode('utf8')

    class Meta:
        verbose_name=(u'Frecuencia')
        verbose_name_plural=(u'Frecuencias')

class Tareas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name=(u'Id Clentes'))
    sitio = models.ForeignKey(Sitios, on_delete=models.CASCADE, verbose_name=(u'Id Sitios'))
    clave = models.ForeignKey(Claves, on_delete=models.CASCADE, verbose_name=(u'Id Claves'))
    frecrastreo = models.ForeignKey(FrecuenciaRastreos, on_delete=models.CASCADE, verbose_name=(u'Id FrecuenciaRastreos'))
    descripcion = models.CharField(max_length=200, verbose_name=(u'descripción'))
    falta = models.DateTimeField(verbose_name=(u'fecha de alta'))
    fbaja = models.DateTimeField(blank=True, null=True, verbose_name=(u'fecha de baja'))

    def __str__(self):
        return self.descripcion.encode('utf8')

    class Meta:
        verbose_name=(u'Tarea')
        verbose_name_plural=(u'Tareas')

class Rastreos(models.Model):
    fechahora = models.DateTimeField(verbose_name=(u'Fecha hora'))
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE, verbose_name=(u'Id Tareas'))

    def __str__(self):
        return unicode(self.fechahora)

    class Meta:
        verbose_name=(u'Rastreo')
        verbose_name_plural=(u'Rastreos')

class Notas(models.Model):
    url = models.CharField(max_length=500, verbose_name=(u'url'))
    titulo = models.CharField(max_length=500, verbose_name=(u'título'))
    rastreo = models.ForeignKey(Rastreos, on_delete=models.CASCADE, verbose_name=(u'Id Rastreos'))

    def __str__(self):
        return self.url
        return self.titulo

    class Meta:
        verbose_name=(u'Nota')
        verbose_name_plural=(u'Notas')
