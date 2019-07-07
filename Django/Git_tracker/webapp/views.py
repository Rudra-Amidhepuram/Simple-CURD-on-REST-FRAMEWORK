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

# view class for Repo 
class RepoView(generics.ListAPIView):
	serializer_class=RepoSerializer
	queryset=Repo.objects.all()

# view class for Event of a paricular repo 
class Repo_events(generics.ListAPIView):
	serializer_class=EventSerializer
	queryset=Event.objects.all()
	filter_backends= (DjangoFilterBackend,)
	filter_fields=('r_id', )

# view class for Events 
class EventsViews(generics.ListAPIView):
	serializer_class=EventSerializer
	queryset=Event.objects.all()

# view class for Actors 
class ActorViews(generics.ListAPIView):
	serializer_class=ActorSerializer
	queryset=Actor.objects.all()

# view class for Actors of a particular Event 
class Actor_events(generics.ListAPIView):
	serializer_class=ActorSerializer
	queryset=Actor.objects.all()
	filter_backends= (DjangoFilterBackend,)
	filter_fields=('e_id', )
# view class to delete/update a particular Event 
class update_delete_event(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer

# view class to add event
class Add_event(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
