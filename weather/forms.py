from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Введите название города', max_length=100)
    units = forms.ChoiceField(
        label='Единицы измерения',
        choices=[('metric', 'Цельсий'), ('imperial', 'Фаренгейт')],
        widget=forms.RadioSelect,
        initial='metric'
    )
