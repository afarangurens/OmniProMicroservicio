import pandas as pd
from API.models import Client, Country, State, City, Store
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404


class Command(BaseCommand):

    help = "import booms"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        # Cambiar el nombre de los Clientes con Id 5, 8 y 9 poor "JULIAN"
        clients_id = [5, 8, 9]

        for id in clients_id:
            curr_client = get_object_or_404(Client, id=id)
            curr_client.name = "Julian"

            curr_client.save()

        clients_id = [1, 7, 6]
        fav_store_id = 5
        fav_store = get_object_or_404(Store, id=fav_store_id)

        for id in clients_id:
            curr_client = get_object_or_404(Client, id=id)
            curr_client.favorite_stor = fav_store
            curr_client.save()