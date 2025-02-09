from django.urls import path, include

urlpatterns = [
    path('authentication/', include('authentication.urls')),
    path('genres/', include('genres.urls')),
    path('actors/', include('actors.urls')),
    path('movies/', include('movies.urls')),
    path('reviews/', include('reviews.urls')),
]