from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('detail/<int:pk>/', views.DetailPageView.as_view(), name = 'show_contact'),
    path('search/', views.search_contact, name = 'search'),
    path('contacts/create', views.ContactCreateView.as_view(), name = 'create'),
    path('contacts/update/<int:pk>', views.ContactUpdateView.as_view(), name = 'update'),
    path('contacts/delete/<int:pk>', views.ContactDeleteView.as_view(), name = 'delete'),
]
