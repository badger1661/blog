from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

def upload_location(instance, filename):
    try:
        id_ = Post.objects.all().latest('id').id + 1
    except ObjectDoesNotExist:
        id_ = "first_post"

    return ("{}/{}".format(id_, filename))


class Post(models.Model):
    post_title = models.CharField(max_length = 120)
    post_content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    post_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    post_image = models.FileField(upload_to=upload_location, null=True, blank=True) #Attachment, related_name = 'files', 

    def __unicode__(self):
        return self.post_title

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("posts:post_display", kwargs= {'post_id': self.id})

    def delete_post(self):
        return reverse("posts:post_delete", kwargs = {'post_id': self.id})

    def edit_post(self):
        return reverse("posts:post_edit", kwargs = {'post_id': self.id})