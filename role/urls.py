from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import debt_collectors_list_view, debt_collector_create_view, debt_collector_udpate_view
from .views import members_list_view, member_create_view, member_udpate_view


urlpatterns = [
    path('debt_collector/', login_required(debt_collectors_list_view), name='debt_collectors_list'),
    path('debt_collector/add/', login_required(debt_collector_create_view), name='debt_collector_add'),
    path('debt_collector/<int:pk>/', login_required(debt_collector_udpate_view), name='debt_collector_update'),
    path('member/', login_required(members_list_view), name='members_list'),
    path('member/add/', login_required(member_create_view), name='member_add'),
    path('member/<int:pk>/', login_required(member_udpate_view), name='member_update'),
]
