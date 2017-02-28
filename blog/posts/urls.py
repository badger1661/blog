from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import (
    post_timeline,
    post_display,
    post_edit,
    post_delete,
    post_create,
    )

urlpatterns = [
    url(r'^$', post_timeline, name = "post_timeline"),
    url(r'^create$', post_create, name = "post_create"), #PostCreate.as_view(template_name="post_form.html"), name = "post_create"),
    url(r'^(?P<post_id>\d+)$', post_display, name="post_display"),
    url(r'^(?P<post_id>\d+)/edit$', post_edit, name = "post_edit"),
    url(r'^(?P<post_id>\d+)/delete$', post_delete, name = "post_delete"),

]
