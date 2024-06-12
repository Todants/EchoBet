from django.shortcuts import render
from rest_framework import viewsets

from .models import Accounts, Listeners, APIKeys
from .serializers import AccountSerializer, KeysSerializer, ListenersSerializer


def index(request):
    return render(request, 'main/index.html')


# -------------- api --------------

class AccountsApi(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer


class KeysApi(viewsets.ModelViewSet):
    queryset = APIKeys.objects.all()
    serializer_class = KeysSerializer


class ListenersApi(viewsets.ModelViewSet):
    queryset = Listeners.objects.all()
    serializer_class = ListenersSerializer
