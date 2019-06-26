from django.urls import path
from .views import IndexView, newsms

urlpatterns = [
        path('', IndexView.as_view()),
        path('new', newsms, name='newsms'),
    ]
