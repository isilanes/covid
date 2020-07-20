from django import forms

from .models import Country, DataPoint


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ["name"]

    def save(self):
        data = self.cleaned_data
        country = Country()
        country.name = data["name"]
        country.save()


class DataPointForm(forms.ModelForm):

    class Meta:
        model = DataPoint
        widgets = {
            "date": forms.DateInput(format="%Y-%m-%d"),
        }
        fields = ["country", "date", "cases", "deaths", "recoveries"]
