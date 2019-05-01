from django.views.generic.list import ListView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.urls import reverse_lazy
from .models import Person, Address


class AddressInline(InlineFormSetFactory):
    model = Address
    fields = '__all__'
    factory_kwargs = {'max_num': 1}


# Create your views here.
class PeopleListView(ListView):
    model = Person
    fields = '__all__'


people_list_view = PeopleListView.as_view()


class PersonCreateView(CreateWithInlinesView):
    model = Person
    inlines = [AddressInline]
    fields = '__all__'
    success_url = reverse_lazy('people_list')


person_create_view = PersonCreateView.as_view()


class PersonUpdateView(UpdateWithInlinesView):
    model = Person
    inlines = [AddressInline]
    fields = '__all__'
    success_url = reverse_lazy('people_list')


person_update_view = PersonUpdateView.as_view()
