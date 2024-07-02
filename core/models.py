from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=122)
    usn=models.CharField(max_length=122)
    sem=models.CharField(max_length=122)

    def __str__(self) -> str:
        return f"{self.name} ({self.usn})"