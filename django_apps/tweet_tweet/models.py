# python imports
import random

# django imports
from django.conf import settings
from django.db import models

# create model from conf settings
User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    # create foreign_key for user
    user = models.ForeignKey(User)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)

    # modify meta data
    class Meta:
        # set ordering to descending order by id
        ordering = ['-id']

    def __str__(self):
        return self.content

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(0, 122),
        }
