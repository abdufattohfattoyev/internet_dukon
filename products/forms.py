from products.models import Category,Product
from django import forms

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"


class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"