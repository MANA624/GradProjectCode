from django.db import models


# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=5000)
    num_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
