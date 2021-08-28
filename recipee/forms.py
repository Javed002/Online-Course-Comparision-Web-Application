from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=300)
    #@recipee = forms.CharField(max_length=50)
    #description = forms.CharField(max_length=50000, widget=forms.Textarea)
    #video = forms.FileField(required=False)
    #status = forms.BooleanField(required=False,disabled=True, widget=forms.HiddenInput)
    #type = forms.CheckboxInput(widget=forms.CheckboxSelectMultiple)
    class Meta():
        model = Items
        #fields = ('name', 'recipee', 'description', 'video', 'status')
        fields = ('name',)