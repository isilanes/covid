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
        country.tag = data["name"].replace(" ", "_").lower()
        country.save()


class DataPointForm(forms.ModelForm):

    class Meta:
        model = DataPoint
        widgets = {
            "date": forms.DateInput(format="%Y-%m-%d"),
        }
        fields = ["country", "date", "cases", "deaths", "recoveries"]

    def save(self):
        data = self.cleaned_data
        data_point = DataPoint()
        data_point.country = data["country"]
        data_point.date = data["date"]
        data_point.cases = data["cases"]
        data_point.deaths = data["deaths"]
        data_point.recoveries = data["recoveries"]
        data_point.save()
