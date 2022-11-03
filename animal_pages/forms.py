from django import forms


class AnimalCreateForm(forms.Form):
    animal_name = forms.CharField(max_length=50)

    descriptions = forms.CharField(max_length=1000)
