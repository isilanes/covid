from django import forms

from .models import Country, Datum


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["name"]

    def save(self):
        data = self.cleaned_data
        country = Country()
        country.name = data["name"]
        country.save()


class DatumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].widget = forms.SelectDateWidget()

    class Meta:
        model = Datum
        fields = ["country", "date", "cases", "deaths", "recoveries"]
