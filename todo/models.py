from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_time = models.DateTimeField(null=True, blank=True)
    task_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)