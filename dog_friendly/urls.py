from django.urls import path
from .views import DogFriendlyListView, DogFriendlyDetailView

urlpatterns = [
    path('', DogFriendlyListView.as_view()),
    path('<int:pk>/', DogFriendlyDetailView.as_view())
]