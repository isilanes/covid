import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Country


@csrf_exempt
@login_required
def get_country_data(request):
    response = {}
    if request.method == "POST":
        payload = request.POST.get("payload", {})
        payload = json.loads(payload)
        exponent = payload["exponent"]
        response = {
            "y": [i**exponent for i in range(6)],
        }

    return JsonResponse(response)
