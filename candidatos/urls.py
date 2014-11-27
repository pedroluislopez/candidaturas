from django.conf.urls import patterns, url

from candidatos import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^confirm/(?P<key>\w+)/$', views.confirm, name='confirm'),
    #url(r'^reset_password/$', views.reset_password, name='reset_password'),
    #url(r'^user/$', views.user, name='user'),
    #url(r'^candidatura/$', views.candidatura, name='candidatura'),
    #url(r'^borrar_candidatura/$', views.borrar_candidatura, name='borrar_candidatura'),
    url(r'^candidato/(?P<username>[\w.@+-]+)/$', views.candidato, name='candidato'),
    url(r'^about/$', views.about, name='about'),
)
