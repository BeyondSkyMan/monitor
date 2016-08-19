from django.conf.urls import patterns, include, url
import views
from rest_framework import routers, serializers,viewsets, urls


router = routers.DefaultRouter()
router.register(r'configuration' , views.ConfigurationViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'monitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'monitor_data/$', views.monitor_data),
    url(r'graph_data/$', views.graph_data),
    url(r'map/$', views.map1),
    url(r'monitor_detail/$', views.graph),
    url(r'echarts/$', views.echart_detail),
    
    
]



