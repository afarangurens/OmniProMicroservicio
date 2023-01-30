from django.forms import ModelForm
from .models import Client, Country, State, City, Store

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
class StateForm(ModelForm):
    class Meta:
        model = State
        fields = '__all__'


class CitytForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'





