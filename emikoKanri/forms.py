from django import forms

from .models import NurseRecord

class NurseRecordForm(forms.ModelForm):

    class Meta:
        model = NurseRecord
        fields = ('nurse_day', 'urine_time', 'urine_volume', 'memo')