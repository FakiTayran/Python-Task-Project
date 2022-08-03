from django import forms
from  .models import Bin

class OperationModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, operation):
        label = operation.name
        return label

class BinForm(forms.ModelForm):
    class Meta:
        model = Bin
        fields = [
            'operation',
            'latitude',
            'longitude',
        ]
        field_classes = {
            'operation': OperationModelChoiceField,
        }

class BinUpdateForm(forms.ModelForm):
    class Meta:
        model = Bin
        fields = [
            'latitude',
            'longitude'
        ]
