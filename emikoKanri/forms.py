from django import forms
from django.forms import ModelForm, Textarea

from .models import NurseRecord

class NurseRecordForm(forms.ModelForm):

    class Meta:
        model = NurseRecord
        fields = ('nurse_day', 'urine_time', 'urine_volume', 'memo')
        widgets = {
            'memo': Textarea(attrs={'cols': 50, 'rows': 4}),
        }
        # 'memo': Textarea(attrs={'cols': 80, 'rows': 20}),