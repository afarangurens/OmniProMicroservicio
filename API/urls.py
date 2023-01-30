from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Operaciones CRUD de la tabla Clientes
    path('client/<str:client_id>', views.client, name='client'),
    path('new-client/', views.create_client, name='create-client'),
    path('see-clients/', views.see_clients, name='see-clients'),
    path('update-client/<str:client_id>', views.update_client, name='update-client'),
    path('delete-client/<str:client_id>', views.delete_client, name='delete-client'),
    
    # Operaciones CRUD de la tabla Países
    path('country/<str:country_id>', views.country, name='country'),
    path('new-country/', views.create_country, name='create-country'),
    path('see-countries/', views.see_countries, name='see-countries'),
    path('update-country/<str:country_id>', views.update_country, name='update-country'),
    path('delete-country/<str:country_id>', views.delete_country, name='delete-country'),

    # Operaciones CRUD de la tabla Estados
    path('state/<str:state_id>', views.state, name='state'),
    path('new-state/', views.create_state, name='create-state'),
    path('see-states/', views.see_states, name='see-states'),
    path('update-state/<str:state_id>', views.update_state, name='update-state'),
    path('delete-state/<str:state_id>', views.delete_state, name='delete-state'),

    # Operaciones CRUD de la tabla Ciudades
    path('city/<str:city_id>', views.city, name='city'),
    path('new-city/', views.create_city, name='create-city'),
    path('see-cities/', views.see_cities, name='see-cities'),
    path('update-city/<str:city_id>', views.update_city, name='update-city'),
    path('delete-city/<str:city_id>', views.delete_city, name='delete-city'),

    # Operaciones CRUD de la tabla Tiendas
    path('store/<str:store_id>', views.store, name='store'),
    path('new-store/', views.create_store, name='create-store'),
    path('see-stores/', views.see_stores, name='see-stores'),
    path('update-store/<str:store_id>', views.update_store, name='update-store'),
    path('delete-store/<str:store_id>', views.delete_store, name='delete-store'),
]