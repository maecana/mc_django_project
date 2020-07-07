from django.db import models

class Tweet(models.Model):
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)

    # modify meta data
    class Meta:
        # set ordering to descending order by id
        ordering = ['-id']

    def __str__(self):
        return self.content