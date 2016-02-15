from django.conf.urls import patterns, url

from jsd_app_name import views

urlpatterns = patterns('',
                       url(r'^$', views.BookList.as_view(), name='book_list'),
                       url(r'^new$', views.BookCreate.as_view(), name='book_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),

                       url(r'^$', views.PictureList.as_view(), name='picture_list'),
                       url(r'^new$', views.PictureCreate.as_view(), name='picture_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.PictureUpdate.as_view(), name='picture_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.PictureDelete.as_view(), name='picture_delete'),

                       url(r'^$', views.FilmList.as_view(), name='film_list'),
                       url(r'^new$', views.FilmCreate.as_view(), name='film_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.FilmUpdate.as_view(), name='film_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.FilmDelete.as_view(), name='film_delete'),

)