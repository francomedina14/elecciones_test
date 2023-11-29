from django.urls import path
from voting.views import *

urlpatterns = [
    path('', ballot.initial_form),
    path('formulario/votacion', ballot.ballot_form, name='ballot_form'),
    path('votar/<voter_id>', ballot.vote, name='vote'),
    path('resultados', result.results, name='results'),
]