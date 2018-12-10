from django.contrib import admin
from django.urls import path, include
from person import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('person.urls'))

    # in progress custom paths
    # path('hello', views.get_hi),
    # path('person/<pid>', views.query_by_id),
    # path('poop', views.create_person)
]
