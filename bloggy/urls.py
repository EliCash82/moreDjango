from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bloggy.views.home', name='home'),
    # url(r'^bloggy/', include('bloggy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', 'blog.views.index'),
    	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/Users/almostanderson/aDjangoTest/django/bloggy/blog/static/media'}),
    url(r'^blog/(?P<post_id>\d+)/$', 'blog.views.post'),
)
