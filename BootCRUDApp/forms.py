from django import forms
from .models import ItemModel

class ItemForm(forms.ModelForm):
    class Meta():
        model = ItemModel
        fields = '__all__'