
from django.urls import path
from . import views


urlpatterns = [
path('', views.contact),
# path('pro', views.pro),
path(r'pro/<data>', views.pro),
path('crispy', views.crispy_form),
]