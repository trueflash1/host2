from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('start_page', start_page, name='start_page'),
    path('add_sprav', add_sprav, name='add_sprav'),
    path('index', replace, name='replace'),
    path('wiev_sprav', wiev_sprav, name='wiev_sprav'),
    path('connect', connect, name='connect'),

    # path('replace', replace, name='index'),
    # path('function1', function1),
]
