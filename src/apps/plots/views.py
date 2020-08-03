from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import core
from .models import Country
from .forms import CountryForm, DataPointForm
from .handle_views.get.insert import handle_insert_get
from .handle_views.post.insert import handle_insert_post


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
def show(request):
    context = {
        "show_active": True,
        "cases_plot": core.get_progress_plot_div(),
        "countries": Country.objects.order_by("name"),
    }

    return render(request, "plots/show.html", context)
