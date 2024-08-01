from django.db import models

class to_do(models.Model):
    todo_heading=models.CharField(max_length=50)
    todo_description=models.TextField()
