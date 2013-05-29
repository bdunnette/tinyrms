from django.conf.urls import patterns, url

from eval import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<eval_id>\d+)/$', views.detail, name='detail'),
)
