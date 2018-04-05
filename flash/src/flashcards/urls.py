from django.urls import path, re_path, include

app_name = 'flashcards'

urlpatterns = [
    path('api/', include('flashcards.api.urls', namespace='flashcards_api')),
]
