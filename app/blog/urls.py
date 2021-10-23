from  django.urls import path
#from  .views import index
from rest_framework import routers
from . import views


router = routers.SimpleRouter()

app_name = 'blog'

urlpatterns = [
    # path('about/', views.home),
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('mix/', views.BlogViewMix.as_view(), name='blog-mix'),
]
