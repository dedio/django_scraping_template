# -*- coding: utf-8 -*-

from django import forms
from django.forms.extras import SelectDateWidget

class Prueba(forms.Form):
    start_date = forms.DateField(widget=SelectDateWidget())
    end_date = forms.DateField(widget=SelectDateWidget())

    def __init__(self, *args, **kwargs):
        super(Prueba, self).__init__(*args, **kwargs)
        self.fields['start_date'].label = "Inicial"
        self.fields['end_date'].label = "Final"
