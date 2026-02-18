from django import forms
from .models import Product

# ✅ ЗАПРЕЩЁННЫЕ СЛОВА (Задание 1)
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ✅ СТИЛИЗАЦИЯ BOOTSTRAP (Задание 3)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control mb-3'
            })
        # Checkbox стилизация
        self.fields['is_published'].widget.attrs.update({
            'class': 'form-check-input ms-2'
        })

    #  АНТИСПAM для названия (Задание 1)
    def clean_title(self):
        title = self.cleaned_data['title'].lower()
        forbidden = [word.lower() for word in FORBIDDEN_WORDS]
        if any(word in title for word in forbidden):
            raise forms.ValidationError("Название содержит запрещённые слова!")
        return self.cleaned_data['title']

    #  АНТИСПAM для описания (Задание 1)
    def clean_description(self):
        desc = self.cleaned_data['description'].lower()
        forbidden = [word.lower() for word in FORBIDDEN_WORDS]
        if any(word in desc for word in forbidden):
            raise forms.ValidationError("Описание содержит запрещённые слова!")
        return self.cleaned_data['description']

    #  ВАЛИДАЦИЯ ЦЕНЫ (Задание 2)
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной!")
        return price
