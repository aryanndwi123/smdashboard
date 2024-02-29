from django.db import models

class SocialMediaPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.title
