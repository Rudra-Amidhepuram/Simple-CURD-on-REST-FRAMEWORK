from rest_framework import serializers
from .models import Repo,Event,Actor

# serializer for Repo model
class RepoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Repo
		fields= '__all__'

# serializer for Event model
class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model=Event
		fields= '__all__'


# serializer for Actor model
class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Actor
		fields= '__all__'
		read_only_fields= ('e_id','r_id', ) 
		depth=3   #it displays the content of "e_id" and "r_id"
