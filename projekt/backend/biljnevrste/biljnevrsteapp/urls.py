from django.urls import path, include
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('biljnevrsteapp',views.BiljneVrsteView)

urlpatterns = [
	# path('', include(router.urls))
	path('', views.index, name='index')
]
