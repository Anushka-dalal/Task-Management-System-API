from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null = True, blank= True)

    def __str__(self):
        return self.title
        # return super().__str__()