from django.urls import path
from electronics_store import views
from electronics_store.apps import ElectronicsStoreConfig


app_name = ElectronicsStoreConfig.name


urlpatterns = [
    path("", views.NetworkMemberListView.as_view(), name='element_list'),
    path("create/", views.NetworkMemberCreateView.as_view(), name='element_create'),
    path("network_member/<pk>", views.NetworkMemberView.as_view(), name='element_detail'),
]