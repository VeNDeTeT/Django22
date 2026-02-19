from django import forms
from .models import Product

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
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input ms-2'})

    def clean(self):
        cleaned_data = super().clean()


        fields_to_check = list(cleaned_data.keys())

        for field_name in fields_to_check:
            value = cleaned_data.get(field_name)
            if isinstance(value, str) and value:
                value_lower = value.lower()
                for word in FORBIDDEN_WORDS:
                    if word in value_lower:
                        self.add_error(field_name, f"Запрещено слово: '{word}'")
                        break


        price = cleaned_data.get('price')
        if price is not None and price < 0:
            self.add_error('price', " Цена не может быть отрицательной!")

        return cleaned_data
