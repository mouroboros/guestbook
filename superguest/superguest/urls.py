from django.conf.urls import include, url
from django.contrib import admin
from guestbook import views as guest_views
from guestbook import urls as guest_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',guest_views.home_page, name='home'),
    ]
