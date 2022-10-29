from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bikes/', views.bikes_index, name='index'),
    path('bikes/<int:bike_id>', views.bikes_detail, name='bike_detail'),
    path('bikes/create/', views.BikeCreate.as_view(), name='bikes_create'),
    path('bikes/<int:pk>/update', views.BikeUpdate.as_view(), name='bikes_update'),
    path('bikes/<int:pk>/delete/', views.BikeDelete.as_view(), name='bikes_delete'),
    path('bikes/<int:bike_id>/add_ride', views.add_ride, name='add_ride'),
    path('routes/', views.RouteList.as_view(), name='routes_index'),
    path('routes/<int:pk>', views.RouteDetail.as_view(), name='route_detail'),
    path('routes/create/', views.RouteCreate.as_view(), name='routes_create'),
    path('routes/<int:pk>/update', views.RouteUpdate.as_view(), name='routes_update'),
    path('routes/<int:pk>/delete/', views.RouteDelete.as_view(), name='routes_delete'),
    path('rides/', views.RideList.as_view(), name='rides_index'),
    path('rides/create/', views.RideCreate.as_view(), name='rides_create'),
    path('rides/<int:ride_id>', views.ride_detail, name='ride_detail'),
    path('rides/<int:pk>/update', views.RideUpdate.as_view(), name='rides_update'),
    path('rides/<int:pk>/delete/', views.RideDelete.as_view(), name='rides_delete'),
    # path('rides/<int:ride_id>/assoc_nutrition/<int:nutrition_id>', views.assoc_nutrition, name='assoc_nutrition')
    path('rides/<int:ride_id>/add_nutrition_plan/', views.add_nutrition_plan, name='add_nutrition_plan')
]
