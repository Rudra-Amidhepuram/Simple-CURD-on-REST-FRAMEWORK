from rest_framework import serializers
from .models import user,Repo,Event,Actor

class userList(serializers.ModelSerializer):

	class Meta:
		model=user
		fields=('id','name','p_name','mobile')


class RepoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Repo
		fields= '__all__'


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model=Event
		fields= '__all__'

class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Actor
		fields= '__all__'

