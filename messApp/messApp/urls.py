from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'messApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^stock/', include('stock.urls')),#url(r'^', include('stock.urls')),
    url(r'^reviewSystem/',include('reviewSystem.urls')), #for  API
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),	#api auth , login logout views
)
