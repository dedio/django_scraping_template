# -*- coding: utf-8 -*-

from django import forms
from django.forms.extras import SelectDateWidget
 
class Prueba(forms.Form):
    start_date = forms.DateField(widget=SelectDateWidget())
    end_date = forms.DateField(widget=SelectDateWidget())
