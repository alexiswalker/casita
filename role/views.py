from django.urls import reverse_lazy
from .models import DebtCollector, Member
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.
class DebtCollectorsListView(ListView):
    model = DebtCollector
    fields = '__all__'


debt_collectors_list_view = DebtCollectorsListView.as_view()


class DebtCollectorCreateView(CreateView):
    model = DebtCollector
    fields = '__all__'
    success_url = reverse_lazy('debt_collectors_list')


debt_collector_create_view = DebtCollectorCreateView.as_view()


class DebtCollectorUpdateView(UpdateView):
    model = DebtCollector
    fields = '__all__'
    success_url = reverse_lazy('debt_collectors_list')


debt_collector_udpate_view = DebtCollectorUpdateView.as_view()


class MembersListView(ListView):
    model = Member
    fields = '__all__'


members_list_view = MembersListView.as_view()


class MemberCreateView(CreateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members_list')


member_create_view = MemberCreateView.as_view()


class MemberUpdateView(UpdateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members_list')


member_udpate_view = MemberUpdateView.as_view()
