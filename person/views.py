from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person


# Create your views here.
class PeopleListView(ListView):
    model = Person
    fields = '__all__'


people_list_view = PeopleListView.as_view()


class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('people_list_view')


person_create_view = PersonCreateView.as_view()


class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('people_list_view')


person_update_view = PersonUpdateView.as_view()
