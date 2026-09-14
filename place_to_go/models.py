from django import forms

class PlaceForm(forms.Form):
    title = forms.CharField(label="Назва", max_length=100, required=True)
    description = forms.CharField(label="Опис", widget=forms.Textarea, required=True)
    place_type = forms.CharField(label="Тип місця", max_length=50, required=True)
    location = forms.CharField(label="Локація", max_length=100, required=False)
    rating = forms.IntegerField(label="Рейтинг", min_value=1, max_value=5, required=True)