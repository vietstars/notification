"""
musicgreed URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	
	## App urls
    url(r'^', include('apps.accounts.urls', namespace='accounts')),
    url(r'^', include('apps.notifications.urls', namespace='notifications')),
    url(r'', include('user_sessions.urls', 'user_sessions')),
    
    ## Admin urls
    url(r'^admin/', admin.site.urls),
]
