from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=64)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return self.name


class Step(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=64)
    position = models.IntegerField()
    track = models.ForeignKey(Track)

    def __unicode__(self):
        return self.name