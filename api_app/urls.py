
from django.urls import path
from .views import *

urlpatterns = [
    path('relacao/',relacao),
    path('relacao/<id>',relacao_id),
]
