from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import people_list_view, person_create_view, person_update_view


urlpatterns = [
    path('', login_required(people_list_view), name='people_list_view'),
    path('add/', login_required(person_create_view), name='person_add'),
    path('<int:pk>/', login_required(person_update_view), name='person_update'),
]
