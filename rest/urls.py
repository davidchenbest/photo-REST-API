from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.restView),
    path('photos', views.photos),
    path('folders', views.folders),
    path('folderPhotos/<str:id>/', views.folderPhotos),

]
