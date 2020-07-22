from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Country


@csrf_exempt
@login_required
def get_country_data(request):
    response = {}
    if request.method == "POST":
        response = {
            "y": [1, 8, 2],
        }

    return JsonResponse(response)
