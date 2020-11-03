import json
import requests
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from apps.plots.models import Country, DataPoint


BASE_URL = "https://covid-api.com/api/reports"


def get_data_for(iso_code, timestamp):
    payload = {
        "iso": iso_code,
        "date": timestamp.strftime("%Y-%m-%d"),
    }
    r = requests.get(BASE_URL, params=payload)

    if r.status_code != 200:
        return None, None

    data = json.loads(r.content)["data"]
    confirmed, deaths, recovered = 0, 0, 0
    for region in data:
        confirmed += region["confirmed"]
        deaths += region["deaths"]
        recovered += region["recovered"]

    return confirmed, deaths, recovered


class Command(BaseCommand):

    help = "Insert DataPoints from online API."

    def add_arguments(self, parser):
        """Extra CLI arguments, if required."""

        parser.add_argument("--country",
                            help="ISO code of Country.",
                            default=None)

        parser.add_argument("--date-from",
                            help="ISO date of start of time range.",
                            default=None)

        parser.add_argument("--date-to",
                            help="ISO date of end of time range.",
                            default=None)

    def handle(self, *args, **kwargs):
        country_iso = kwargs.get("country")
        start_date = kwargs.get("date_from")
        end_date = kwargs.get("date_to")
        if end_date is None:
            end_date = start_date

        country = Country.objects.get(iso=country_iso)

        timestamp = datetime.strptime(start_date, "%Y-%m-%d")
        timestamp_end = datetime.strptime(end_date, "%Y-%m-%d")
        while timestamp <= timestamp_end:
            # Skip DataPoints already in db:
            if DataPoint.objects.filter(country=country, date=timestamp).exists():
                print(timestamp, country, "skip")
                timestamp += timedelta(days=1)
                continue

            cases, deaths, recoveries = get_data_for(country_iso, timestamp)

            data_point = DataPoint(country=country,
                                   date=timestamp,
                                   cases=cases,
                                   deaths=deaths,
                                   recoveries=recoveries)
            data_point.save()

            print(data_point, data_point.cases, data_point.deaths)

            timestamp += timedelta(days=1)
