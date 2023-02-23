from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import User

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer