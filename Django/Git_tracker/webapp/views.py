from django.shortcuts import render
from rest_framework import generics
from .models import Repo,Event,Actor
from .import models
from .import serializers
from .serializers import ActorSerializer,RepoSerializer,EventSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
# queryset = user.objects.all()
#serializer_class = userList

class RepoView(generics.ListAPIView):
	serializer_class=RepoSerializer
	queryset=Repo.objects.all()
class Repo_events(generics.ListAPIView):
	serializer_class=EventSerializer
	queryset=Event.objects.all()
	filter_backends= (DjangoFilterBackend,)
	filter_fields=('r_id', )

class EventsViews(generics.ListAPIView):
	serializer_class=EventSerializer
	queryset=Event.objects.all()

class ActorViews(generics.ListAPIView):
	serializer_class=ActorSerializer
	queryset=Actor.objects.all()
	
class Actor_events(generics.ListAPIView):
	serializer_class=ActorSerializer
	queryset=Actor.objects.all()
	filter_backends= (DjangoFilterBackend,)
	filter_fields=('e_id', )

class update_delete_event(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer


class Add_event(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
