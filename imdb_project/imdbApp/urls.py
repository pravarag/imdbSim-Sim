

from django.conf.urls import patterns, url


from imdbApp import views


urlpatterns=patterns('',
		url(r'^$', views.user_login, name='login'),
		url(r'^logout/$', views.user_logout, name='logout'),
		url(r'^register/$', views.register, name='register'),
		url(r'^dashboard/$', views.dashboard, name='dashboard'),
		url(r'^movie_search/$', views.movie_search, name='movie_search'),
		url(r'^movie_info/$', views.movie_search, name='movie_info'),
		url(r'^movie_search_byId/$', views.movie_search_byId, name="movie_search_byId"),
		url(r'^movie_by_id/$', views.movie_search_byId, name="movie_by_id"),
	)