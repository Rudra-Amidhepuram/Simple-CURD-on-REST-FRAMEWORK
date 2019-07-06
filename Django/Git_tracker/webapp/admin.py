from django.contrib import admin

from .models import	user,Repo,Event,Actor

admin.site.register(user)
admin.site.register(Repo)
admin.site.register(Event)
admin.site.register(Actor)