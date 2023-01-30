import pandas as pd
from API.models import Client, Country, State, City, Store
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
import random


class Command(BaseCommand):

    help = "import booms"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        
        # DATA INSERT FOR COUNTRY TABLE
        country_data = pd.read_excel('insert_data.xlsx', sheet_name="countries")
        for name, code in zip(
            country_data.name, country_data.code):
            curr_country = Country(name=name, code=code)

            curr_country.save()
        
        # DATA INSERT FOR STATE TABLE
        state_data = pd.read_excel('insert_data.xlsx', sheet_name="states")
        for name, code, country in zip(
            state_data.name, state_data.code, state_data.country):
            curr_country = get_object_or_404(Country, id=country)

            state = State(name=name, code=code, country=curr_country )

            state.save()
        
        # DATA INSERT FOR CITY TABLE
        city_data = pd.read_excel('insert_data.xlsx', sheet_name="cities")
        for name, code, state in zip(
            city_data.name, city_data.code, city_data.state):
            curr_state = get_object_or_404(State, id=state)

            city = City(name=name, code=code, state=curr_state )

            city.save()

        # DATA INSERT FOR CITY TABLE
        store_data = pd.read_excel('insert_data.xlsx', sheet_name="stores")
        for name, code in zip(
            store_data.name, store_data.code):

            store = Store(name=name, code=code)

            store.save()
        
        # DATA INSERT FOR CLIENT TABLE
        store_data = pd.read_excel('insert_data.xlsx', sheet_name="clients")
        for name, surname, country, state, city, store in zip(
            store_data.name, store_data.surname, store_data.country, store_data.state, store_data.city, store_data.store):
            curr_country = get_object_or_404(Country, id=country)
            curr_state = get_object_or_404(State, id=state)
            curr_city = get_object_or_404(City, id=city)
            curr_store = get_object_or_404(Store, id=store)

            client = Client(name=name, surname=surname, country=curr_country, state=curr_state, city=curr_city, favorite_stor=curr_store)

            client.save()