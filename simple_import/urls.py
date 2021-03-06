from django.conf.urls import url
from simple_import import views
from django.urls import path

app_name = 'simple_import'

urlpatterns = [
    path('start_import/', views.start_import, name='simple_import-start_import'),
    url('^match_columns/(?P<import_log_id>\d+)/$', views.match_columns, name='simple_import-match_columns'),
    url('^match_relations/(?P<import_log_id>\d+)/$', views.match_relations, name='simple_import-match_relations'),
    url('^do_import/(?P<import_log_id>\d+)/$', views.do_import, name='simple_import-do_import'),
]
