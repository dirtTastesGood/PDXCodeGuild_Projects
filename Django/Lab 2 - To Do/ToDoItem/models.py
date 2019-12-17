from django.db import models

class ToDoItem(models.Model):
    task_text = models.CharField(max_length=200)

    created_at = models.DateTimeField('date_published')

    completed = models.BooleanField(default=False)

    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.task_text
