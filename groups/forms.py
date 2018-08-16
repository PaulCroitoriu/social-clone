from django import forms

from .models import Group

class GroupForm(forms.ModelForm):
    name = forms.CharField(label='',
            widget=forms.TextInput(attrs={'placeholder':'name your group'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={
                                        'placeholder':'add a short description',
                                        'rows':2
                                        }))


    class Meta:
        model = Group
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
