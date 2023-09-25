from django.db import models

# Create your models here.
#storing task as data. clicking on add stores it as
#uncompleted. 
#click mark as completed button
#need a field to store whether its completed or not. 
#needs 2 db fields. 


class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task