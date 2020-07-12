from django.contrib import admin
from .models import Tweet


# class TweetForm(admin.ModelAdmin):
#     class Meta:
#         model = Tweet
#         fields = ['content', 'user_id', 'username']
    
#     def __str__(self):
#         return self.user

admin.site.register(Tweet)