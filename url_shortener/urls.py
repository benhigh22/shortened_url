"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from url_app.views import FirstView, redirect, BookmarkListView, BookmarkDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', FirstView.as_view(), name="first_view"),
    url(r'^list/', BookmarkListView.as_view(), name="bookmark_list_view"),
    url(r'^b/(?P<url>\w+)', redirect),
    url(r'^newurl/', FirstView.as_view(), name="new_url"),
    url(r'^detail/(?P<pk>\d+)', BookmarkDetailView.as_view(), name="detail_view")
]

