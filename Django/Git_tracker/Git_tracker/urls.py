from django.contrib import admin
from django.urls import path, re_path, include
from webapp.views import RepoView


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('webapp.urls')),
	re_path('', RepoView.as_view()),
]
