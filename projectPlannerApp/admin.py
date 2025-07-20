from django.contrib import admin
from .models import Project, Tag, Task, Comment
# Register your models here.

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Comment)