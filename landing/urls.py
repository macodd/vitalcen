from django.urls import path

from .views import vitalcen_landing_view, terms_view

app_name = 'landing'

urlpatterns = [
    path('', vitalcen_landing_view, name='home'),
    path('terms/', terms_view, name='terms')
]
