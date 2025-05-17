from django.urls import path

from app1.views import simple1
urlpatterns = [
    path('sim1/',simple1),
]