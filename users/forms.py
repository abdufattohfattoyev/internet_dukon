from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from products.models import Cart
from .models import User
from django import forms


class UserRegisterForm(forms.ModelForm):
    password1=forms.CharField(label="Parol kiriting",widget=forms.PasswordInput)
    password2=forms.CharField(label="Parolni tasdiqlang",widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=("username","email","password1","password2")

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")


        if password1 and password2 and password1 != password2:
            raise ValidationError("Parollar bir biriga mos emas")
        return password1


# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(label="Foydalanuvchi nomi", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(label="Foydalanuvchi nomi")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput())

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get("username")
        password=cleaned_data.get("password")



        if username or password:
            user=User.objects.filter(username=username).first()
            if user is None or not user.check_password(password):
                raise ValidationError("username yoki parol xato")
        return cleaned_data


class CartForm(forms.Form):
    product_qty = forms.IntegerField(
        min_value=1,
        label="Miqdor",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )