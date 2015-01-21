from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'django.contrib.auth.views.login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'make_friends.views.login_work', name='login'),
   # url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^register/', 'make_friends.views.register', name='register'),
    url(r'^account/', 'make_friends.views.account', name='account'),
    #url(r'^logout/', 'make_friends.views.logout', name='logout'),"""
)
