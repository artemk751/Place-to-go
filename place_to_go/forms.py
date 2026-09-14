from django import forms


class PlaceForm(forms.Form):
    title = forms.CharField(
        label='Назва',
        max_length=200,
        error_messages={'required': 'Назва не може бути порожньою'}
    )
    description = forms.CharField(
        label='Опис',
        widget=forms.Textarea
    )
    place_type = forms.CharField(
        label='Тип місця',
        max_length=100
    )
    location = forms.CharField(
        label='Локація',
        max_length=300,
        required=False
    )
    rating = forms.IntegerField(
        label='Рейтинг (1-5)',
        min_value=1,
        max_value=5
    )