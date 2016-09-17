from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.addArticle, name="addArticle"),
    url(r'^addNewspaper$', views.addNewspaper, name="addNewspaper"),
]