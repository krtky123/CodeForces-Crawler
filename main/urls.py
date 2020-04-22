from django.urls import path
from . import views as v
from .views import HomePageView

urlpatterns = [
    path('', v.HomePageView.as_view(), name='home'),
]