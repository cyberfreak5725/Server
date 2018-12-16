"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^$', 'django.contrib.auth.views.login'),
#  url(r'^logout/$', logout_page),
#  url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
#  url(r'^register/$', register),
#  url(r'^register/success/$', register_success),
#  url(r'^home/$', home),
# ]



from django.conf.urls import include, url

from django.contrib.auth import views as auth_views
from login import views as myapp_views
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    # url(r'^$', myapp_views.home, name='home'),
    # url(r'^contact/$', myapp_views.contact, name='contact'),
    # url(r'^login/$', auth_views.login, name='login'),
    url(r'^$',auth_views.LoginView.as_view(template_name="login.html"),name='login'),
 url(r'^logout/$', myapp_views.logout_page,name='logout'),
 url(r'^accounts/login/$',auth_views.LoginView.as_view(template_name="login.html"),name='login'), # If user is not login it will redirect to login page
 url(r'^register/$',  myapp_views.register,name='register'),
 url(r'^register/success/$', myapp_views.register_success,name='success'),
 url(r'^home/$', myapp_views.home,name='home'),
 # url(r'^verified-email-field/', include('verified_email_field.urls')),

]