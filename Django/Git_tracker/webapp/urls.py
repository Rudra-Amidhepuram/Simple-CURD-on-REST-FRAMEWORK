from django.urls import path,include
from .views import RepoView,Repo_events,EventsViews,ActorViews,Actor_events,update_delete_event,Add_event







urlpatterns = [
    
	path('repo/', RepoView.as_view(), name="repo-all"),
	path('rep/', Repo_events.as_view(), name="repo_events-all"),
	path('actor_events/', Actor_events.as_view(), name="Actor_events-all"),
	path('events/',EventsViews.as_view(), name="ALL Events"),
	path('actors/',ActorViews.as_view(), name="ALL Actros"),
        path('event/<int:pk>/', update_delete_event.as_view()),
	path('add/',Add_event.as_view())
	
]
