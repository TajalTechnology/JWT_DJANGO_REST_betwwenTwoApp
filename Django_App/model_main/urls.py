from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),
    path('api/data', views.api_data, name='api-data'),
    path('api/comunication/', views.TakeJWTPayload.as_view(), name='api-data'),



]
