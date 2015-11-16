from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^$', views.home,
            name='home'), 
	url(r'^writings/$', views.writings,
            name='writings'),
	url(r'^photography/$', views.photography,
            name='photography'),
	url(r'^submit/$', views.submit,
            name='submit'),
	url(r'^pastwinners/$', views.pastwinners,
            name='pastwinners'),
	url(r'^submitwritings/$', views.submitwritings,
            name='submitwritings'),
    	url(r'^submitdrawings/$', views.submitdrawings,
            name='submitdrawings'),
    	url(r'^submitphotography/$', views.submitphotography,
            name='submitphotography'),
	url(r'^submitstuff/$', views.submitstuff,
            name='submitstuff'),
	url(r'^upload_picture/$', views.upload_picture,
            name='upload_picture'),
	url(r'^vote_a/$', views.submitstuff,
            name='submitstuff'),
    	url(r'^loginpage/$', views.loginpage,
            name='loginpage'),
	url(r'^userlogin/$', views.userlogin,
            name='userlogin'),
	url(r'^new_user_page/$', views.new_user_page,
            name='new_user_page'),
	url(r'^newuser/$', views.newuser,
            name='newuser'),
    	url(r'^log_out/$', views.log_out,
            name='log_out'),
]


