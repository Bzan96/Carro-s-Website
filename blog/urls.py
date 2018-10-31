from django.urls import include, path
from . import views
from .feeds import PostsFeed

from .views import emailView, successView

urlpatterns = [
	path("index", views.post_list_view, name="post_list_view"),
	path(r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$", views.post_detail_view, name="post_detail_view"),
	path(r"^feed/$", PostsFeed(), name="post_feed"),
]

urlpatterns += [
	path("index", views.index, name="index"),
	path("bröllop", views.wedding, name="wedding"),
	path("fancy", views.fancy, name="fancy"),
	path("fransar", views.fransar, name="fransar"),
	path("om_mig", views.om_mig, name="om_mig"),
	path("kontakt", emailView, name="kontakt"),
	path("emailsuccess", successView, name="emailsuccess"),
]