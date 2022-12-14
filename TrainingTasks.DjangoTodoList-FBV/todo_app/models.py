from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return "[" + self.title + "]"