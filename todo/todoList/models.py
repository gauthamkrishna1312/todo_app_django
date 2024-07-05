from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

User = get_user_model()

class todoCharts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user who created the todo.
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
