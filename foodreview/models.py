from django.db import models
from django.utils import timezone

# Create your models here.
class Menu(models.Model):
    menu = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.TextField()
    price = models.IntegerField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.menu

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    menu = models.ForeignKey(Menu, related_name='comments', on_delete=models.CASCADE)