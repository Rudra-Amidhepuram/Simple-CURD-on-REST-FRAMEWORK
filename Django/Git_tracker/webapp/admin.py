from django.contrib import admin

from .models import	Repo,Event,Actor

admin.site.register(Repo)
admin.site.register(Event)
admin.site.register(Actor)
