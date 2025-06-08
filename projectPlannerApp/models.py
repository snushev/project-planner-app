from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):

    """Define Project object"""

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    """Define Tag object"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):

    """Define Task object"""

    CHOICES = [
        ("TODO", "TODO"),
        ("IN_PROGRESS", "IN_PROGRESS"),
        ("DONE", "DONE")
    ]
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=20, choices=CHOICES, default='TODO')
    deadline = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField(Tag, related_name='tasks')

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Define Comment model"""

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment