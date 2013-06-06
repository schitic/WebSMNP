from django.conf.urls import patterns, include, url
from profiles import views

urlpatterns = patterns('',
    url(r'^test/',views.test_variable),

)
