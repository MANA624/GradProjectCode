from django.db import models


# Create your models here.
class Thread(models.Model):
    topic = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.topic

    def __add__(self, other):
        return self.__str__() + other


class Response(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.thread + ": " + self.content[:15]
