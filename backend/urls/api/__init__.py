from django.urls import path, include

urlpatterns = [
    path('', include('backend.urls.api.v1'))
]
