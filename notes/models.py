from django.db import models

class Task(models.Model):
    status = {
        "1": "yomon",
        "2" : "yaxshi",
        "3": "alo",
        "4": "super"
    }
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, default="", null=True)
    statuse = models.CharField(choices=status, default="2")

    def __str__(self):
        return f" {self.id} : {self.name}"



