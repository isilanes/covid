from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ...models import Country, DataPoint
from ...forms import CountryForm, DataPointForm


@login_required
def handle_insert_get(request):
    initial = {
        "date": datetime.now() - timedelta(days=1),  # usually we insert data from yesterday
    }
    latest_data_points = []
    for country in Country.objects.all():
        latest = DataPoint.objects.filter(country=country).order_by("date").last()
        if latest is not None:
            latest_data_points.append((country, latest))

    latest_data_points = [l for _, l in sorted(latest_data_points)]

    context = {
        "insert_active": True,
        "country_form": CountryForm(),
        "datum_form": DataPointForm(initial=initial),
        "countries": Country.objects.order_by("name"),
        "latest_data_points": latest_data_points,
    }

    return render(request, "plots/insert.html", context)
