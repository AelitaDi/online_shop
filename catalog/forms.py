from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from .models import Product

BAD_WORDS = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'category',)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'placeholder': 'Введите наименование продукта'
        })

        self.fields['description'].widget.attrs.update({
            'placeholder': 'Введите описание продукта'
        })

        self.fields['price'].widget.attrs.update({
            'placeholder': 'Введите стоимость'
        })

    def clean_image(self):
        imagesize = self.cleaned_data.get('image').size
        if imagesize > 5242880:
            raise ValidationError("Вы не можете загрузить файл больше 5Mb")
        return self.cleaned_data.get('image')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in BAD_WORDS:
            if word in name.lower():
                raise ValidationError(f'Наименование продукта не может содержать слово {word.upper()}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in BAD_WORDS:
            if word in description.lower():
                raise ValidationError(f'Наименование продукта не может содержать слово {description.upper()}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Стоимость продукта не может быть меньше 0')
        return price
