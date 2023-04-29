from django.urls import path
from .views import FavouriteListView, FavouriteDetailView

urlpatterns = [
    path('', FavouriteListView.as_view()),
    path('<int:pk>/', FavouriteDetailView.as_view())
]