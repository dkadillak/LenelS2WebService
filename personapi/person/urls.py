from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('person', views.PersonView)

urlpatterns = [
    # generates the urls for basic api requests
    path('', include(router.urls))
]
