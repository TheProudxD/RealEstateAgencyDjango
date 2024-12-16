from django import forms

from agencies.models import Agent, Agreement, Message
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class FilterAgentForm(forms.Form): 
    name = forms.CharField(label='Имя', max_length=50, required=False)
    agreement = forms.ModelChoiceField(label='Договор', queryset=Agreement.objects.all(), empty_label='', required=False)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'contact-input', 'placeholder': 'Ваш email'}),
            'subject': forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'Тема сообщения'}),
            'message': forms.Textarea(attrs={'class': 'contact-textarea', 'placeholder': 'Ваше сообщение'})
        }