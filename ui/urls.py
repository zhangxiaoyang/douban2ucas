from django.conf.urls import patterns, include, url
from ui import views, apis

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^auth/', views.auth),
    url(r'^bye/', views.bye),
    url(r'^sorry/', views.sorry),

    url(r'^apis/wish/', apis.wish),
    url(r'^apis/read/', apis.read),
    url(r'^apis/reading/', apis.reading),
    url(r'^apis/ucas/(.\w+)/', apis.ucas),
)
