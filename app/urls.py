
from django.contrib import admin
from django.urls import path
from genres.views import GenreCreatListView, GernreRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreatListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GernreRetrieveUpdateDestroyView.as_view(), name='genre-detail-list'),
]
