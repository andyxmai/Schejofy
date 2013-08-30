from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'schedule.views.home', name='home'),
    # url(r'^schedule/', include('schedule.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'scheduleApp.views.index', name='index'),
    url(r'^home/$', 'scheduleApp.views.home'),
    url(r'^course/(\d+)$', 'scheduleApp.views.course'),
    url(r'^user/(\d+)$', 'scheduleApp.views.user'),
    url(r'^add_course/$', 'scheduleApp.views.add_course'),
    url(r'^remove_course/$', 'scheduleApp.views.remove_course'),
    url(r'^change_shopping/$', 'scheduleApp.views.change_shopping'),
    url(r'^register_form/$', 'scheduleApp.views.register_form'),
    url(r'^register/$', 'scheduleApp.views.register'),
    url(r'^search/$', 'scheduleApp.views.search'),
)

# urlpatterns += staticfiles_urlpatterns()
