from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as authViews
urlpatterns = [
    url(r'^signup/$', views.signup, name= 'signup'),
    url(r'^login/$',views.login_user,name="login.html"),
    url(r'^logout/$',authViews.logout,{'template_name':'userauth/logout.html'})
]