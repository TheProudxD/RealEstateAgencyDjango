from django import forms

from agencies.models import Agent

class AddAgentForm(forms.ModelForm):
    fields = ['name', 'credit', 'photo', 'agreement', 'slug']
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['agreement'].empty_label = 'Не выбран'

    def clean_name(self):
        first_name = self.cleaned_data['name']
        if not first_name.isalpha():
            raise forms.ValidationError('Недопустимые символы в ФИО')
        return first_name

    class Meta: 
        model = Agent  
        fields = '__all__'