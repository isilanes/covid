from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
    """Main view."""

    context = {
    }

    return render(request, "plots/main.html", context)
