from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import people_list_view


urlpatterns = [
    path('', login_required(people_list_view), name='people_list_view'),
]
