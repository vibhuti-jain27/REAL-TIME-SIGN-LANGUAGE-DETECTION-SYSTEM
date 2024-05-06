from django.urls import path
from . import views
app_name = 'frontends'
urlpatterns = [
    path('', views.index, name='index'),  # URL for the index view
]