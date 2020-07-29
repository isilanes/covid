import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Country, DataPoint


@csrf_exempt
@login_required
def get_country_data(request):
    response = {}
    if request.method == "POST":
        payload = request.POST.get("payload", {})
        payload = json.loads(payload)
        country_list = payload["country_list"]
        for country_name in country_list:
            data_points = DataPoint.objects.filter(country__tag=country_name).order_by("date")
            response[country_name] = {
                "x": [dp.date for dp in data_points],
                "y": [dp.cases for dp in data_points],
            }

    return JsonResponse(response)
