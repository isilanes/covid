import os
from datetime import datetime

from django.core.management.base import BaseCommand

from apps.plots.models import Country, DataPoint


class Command(BaseCommand):

    help = "Insert DataPoints for a Country from its CVS."

    def add_arguments(self, parser):
        """Extra CLI arguments, if required."""

        parser.add_argument("--country",
                            help="Name of Country.",
                            default=None)

        parser.add_argument("--data-dir",
                            help="Directory with data.",
                            default=None)

    def handle(self, *args, **kwargs):
        country_name = kwargs.get("country")
        data_dir = kwargs.get("data_dir")

        country = Country.objects.get(name=country_name)
        csv_path = os.path.join(data_dir, f"{country.tag}.csv")

        with open(csv_path) as f:
            f.readline()  # ignore first line
            for line in f:
                timestamp, cases, deaths, recoveries = line.split(",")
                timestamp = f"2020/{timestamp}"
                timestamp = datetime.strptime(timestamp.replace('"', ''), "%Y/%d/%m")
                cases = int(cases.replace('"', ''))
                deaths = int(deaths.replace('"', ''))
                recoveries = int(recoveries.replace('"', ''))

                data_point = DataPoint(country=country,
                                       date=timestamp,
                                       cases=cases,
                                       deaths=deaths,
                                       recoveries=recoveries)
                data_point.save()

