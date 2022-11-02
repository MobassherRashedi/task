from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        
    def __str__(self) -> str:
        return f"{self.id}-{self.name}"