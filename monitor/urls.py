from django.conf.urls import  include, url
from django.contrib import admin
from web import views 
urlpatterns = [
    # Examples:
    # url(r'^$', 'monitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls')),
    #url(r'^map/$', views.map1),
    #url(r'^monitor_detail/$', views.graph),
    url(r'login', include('login.urls')),
]

