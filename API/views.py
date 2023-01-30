from django.shortcuts import render, redirect
from .models import Client, Country, State, City, Store
from .forms import ClientForm, CountryForm, StateForm, CitytForm, StoreForm

# CREATE 
def create_client(request):
    form =  ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'create_client.html', context)

def create_country(request):
    form =  CountryForm()

    if request.method == 'POST':
        form = CountryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'create_country.html', context)

def create_state(request):
    form =  StateForm()

    if request.method == 'POST':
        form = StateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'create_state.html', context)

def create_city(request):
    form =  CitytForm()

    if request.method == 'POST':
        form = CitytForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'create_city.html', context)

def create_store(request):
    form =  StoreForm()

    if request.method == 'POST':
        form = StoreForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'create_store.html', context)

# READ ALL ITEMS

def see_clients(request):
    clients = Client.objects.all()
    context = {"clients": clients}

    return render(request, 'see_clients.html', context)
    
def see_countries(request):
    countries = Country.objects.all()
    context = {"countries": countries}

    return render(request, 'see_countries.html', context)
    
def see_states(request):
    states = State.objects.all()
    context = {"states": states}

    return render(request, 'see_states.html', context)
    
def see_cities(request):
    cities = City.objects.all()
    context = {"cities": cities}

    return render(request, 'see_cities.html', context)
    
def see_stores(request):
    stores = Store.objects.all()
    context = {"stores": stores}

    return render(request, 'see_stores.html', context)

# READ INDIVIDUA ITEM
def client(request, client_id):
    client = Client.objects.get(id=client_id)
    context = {'client': client}

    return render(request, 'client.html', context)

def country(request, country_id):
    country = Country.objects.get(id=country_id)
    context = {'country': country}

    return render(request, 'country.html', context)

def state(request, state_id):
    state = State.objects.get(id=state_id)
    context = {'state': state}

    return render(request, 'state.html', context)

def city(request, city_id):
    city = State.objects.get(id=city_id)
    context = {'city': city}

    return render(request, 'city.html', context)

def store(request, store_id):
    store = Store.objects.get(id=store_id)
    context = {'store': store}

    return render(request, 'store.html', context)

# UPDATE 

def update_client(request, client_id):
    try: 
        client_to_update = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return redirect('home')

    client_form = ClientForm(request.POST or None, instance=client_to_update)
    if client_form.is_valid():
        client_form.save()
        return redirect('home')
    context = {'client': client_form}

    return render(request, 'update_client.html', context)

def update_country(request, country_id):
    try: 
        country_to_update = Country.objects.get(id=country_id)
    except Country.DoesNotExist:
        return redirect('home')

    country_form = CountryForm(request.POST or None, instance=country_to_update)
    if country_form.is_valid():
        country_form.save()
        return redirect('countries.html')
    context = {'country': country_form}

    return render(request, 'update_country.html', context)

def update_state(request, state_id):
    try: 
        state_to_update = State.objects.get(id=state_id)
    except State.DoesNotExist:
        return redirect('home')

    state_form = StateForm(request.POST or None, instance=state_to_update)
    if state_form.is_valid():
        state_form.save()
        return redirect('home')
    context = {'state': state_form}

    return render(request, 'update_state.html', context)

def update_city(request, city_id):
    try: 
        city_to_update = City.objects.get(id=city_id)
    except City.DoesNotExist:
        return redirect('home')

    city_form = CitytForm(request.POST or None, instance=city_to_update)
    if city_form.is_valid():
        city_form.save()
        return redirect('home')
    context = {'city': city_form}

    return render(request, 'update_city.html', context)

def update_store(request, store_id):
    try: 
        store_to_update = Store.objects.get(id=store_id)
    except Store.DoesNotExist:
        return redirect('home')

    store_form = StoreForm(request.POST or None, instance=store_to_update)
    if store_form.is_valid():
        store_form.save()
        return redirect('home')
    context = {'store': store_form}

    return render(request, 'update_store.html', context)
# DELETE

def delete_client(request, client_id):
    try:
        client_to_delete = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return redirect('home')
    
    client_to_delete.delete()

    return redirect('home')

def delete_country(request, country_id):
    try:
        country_to_delete = Country.objects.get(id=country_id)
    except Country.DoesNotExist:
        return redirect('home')
    
    country_to_delete.delete()

    return redirect('home')
    

def delete_state(request, state_id):
    try:
        state_to_delete = State.objects.get(id=state_id)
    except State.DoesNotExist:
        return redirect('home')
    
    state_to_delete.delete()

    return redirect('home')
    
def delete_city(request, city_id):
    try:
        city_to_delete = City.objects.get(id=city_id)
    except City.DoesNotExist:
        return redirect('home')
    
    city_to_delete.delete()

    return redirect('home')
    
def delete_store(request, store_id):
    try:
        store_to_delete = Store.objects.get(id=store_id)
    except Store.DoesNotExist:
        return redirect('home')
    
    store_to_delete.delete()

    return redirect('home')

def home(request):
    return render(request, 'home.html')

def get_all_cities_in_a_state(request, state_id):
    state = State.objects.get(id=state_id)
    cities = state.city_set.all()

    context = {"cities": cities}

    return render(request, 'see_cities.html', context)


def get_all_store_clients(request, store_id):
    store = Store.objects.get(id=store_id)
    clients = store.client_set.all()

    context = {"clients": clients}

    return render(request, 'see_clients.html', context)

def get_all_clients_given_state(request, state_id):
    state = State.objects.get(id=state_id)
    clients = state.city_set.all()

    context = {"clients": clients}

    return render(request, 'see_clients.html', context)