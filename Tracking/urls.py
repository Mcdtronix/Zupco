from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('update_gps_data/<int:bus_id>/', views.update_gps_data, name='update_gps_data'),

]
