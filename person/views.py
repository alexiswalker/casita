from django.views.generic.list import ListView
from .models import Person


# Create your views here.
class PeopleListView(ListView):
    model = Person


people_list_view = PeopleListView.as_view()
