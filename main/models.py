from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return name