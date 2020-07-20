from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Country
from .forms import CountryForm


@login_required
def insert(request):
    if request.method != "POST":
        return handle_insert_get(request)

    if request.POST.get("country_form") is not None:
        return handle_insert_country_post(request)

    return handle_insert_get(request)


@login_required
def handle_insert_get(request):

    context = {
        "insert_active": True,
        "country_form": CountryForm(),
        "countries": Country.objects.order_by("name"),
    }

    return render(request, "plots/insert.html", context)


@login_required
def handle_insert_country_post(request):
    form = CountryForm(request.POST)
    if form.is_valid():
        form.save()

    return handle_insert_get(request)


@login_required
def show(request):
    context = {
        "show_active": True,
    }

    return render(request, "plots/show.html", context)
