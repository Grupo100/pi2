from django import forms

from .models import Doador, Documento


class UploadForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('titulo', 'doador', 'pdf')