from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import core
from .models import Country, DataPoint
from .forms import CountryForm, DataPointForm


@login_required
def insert(request):
    if request.method != "POST":
        return handle_insert_get(request)

    if request.POST.get("country_form") is not None:
        return handle_insert_post(request, CountryForm)

    if request.POST.get("datapoint_form") is not None:
        return handle_insert_post(request, DataPointForm)

    return handle_insert_get(request)


@login_required
def handle_insert_get(request):

    initial = {
        "date": datetime.now() - timedelta(days=1),  # because data we will insert is usually from yesterday
    }
    latest_data_points = []
    for country in Country.objects.all():
        latest = DataPoint.objects.filter(country=country).order_by("date").last()
        if latest is not None:
            latest_data_points.append((latest.date, country, latest))

    latest_data_points = [l for _, _, l in sorted(latest_data_points, reverse=True)]

    context = {
        "insert_active": True,
        "country_form": CountryForm(),
        "datum_form": DataPointForm(initial=initial),
        "countries": Country.objects.order_by("name"),
        "latest_data_points": latest_data_points,
    }

    return render(request, "plots/insert.html", context)


@login_required
def handle_insert_post(request, WhichForm):
    form = WhichForm(request.POST)
    if form.is_valid():
        form.save()

    return handle_insert_get(request)


@login_required
def show(request):
    context = {
        "show_active": True,
        "cases_plot": core.get_progress_plot_div(),
        "countries": Country.objects.order_by("name"),
    }

    return render(request, "plots/show.html", context)
