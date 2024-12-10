from django.urls import path
from .views import RegisterView, SpamMarkingView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('spam/', SpamMarkingView.as_view(), name='spam'),
]
