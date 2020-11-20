from django import forms

from accused_app.models import Accused


class AccusedForm(forms.ModelForm):
    class Meta:
        model = Accused()
