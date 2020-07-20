from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def insert(request):
    """Main view."""

    context = {
        "insert_active": True,
    }

    return render(request, "plots/insert.html", context)


@login_required
def show(request):
    context = {
        "show_active": True,
    }

    return render(request, "plots/show.html", context)
