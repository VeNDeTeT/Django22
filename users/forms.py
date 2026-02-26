from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm  # ✅ ДОБАВИТЬ

class UserLoginForm(AuthenticationForm):
    """
    Форма авторизации по email
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Меняем label для email поля
        self.fields['username'].label = 'Email'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })


class UserRegistrationForm(UserCreationForm):
    """
    Форма регистрации пользователя
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+7 (999) 123-45-67'
        })
    )
    country = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Россия'
        })
    )

    class Meta:
        model = CustomUser  # Изменено: CustomUser
        fields = ('email', 'phone', 'country', 'password1', 'password2')  # phone вместо phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  # Используем email как username
        if commit:
            user.save()
        return user


class UserProfileForm(UserChangeForm):
    """
    Форма редактирования профиля
    """
    class Meta:
        model = CustomUser  # Изменено: CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone', 'country', 'avatar')  # phone вместо phone_number
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),  # phone вместо phone_number
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
