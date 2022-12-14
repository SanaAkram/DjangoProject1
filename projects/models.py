from django.db import models
import uuid
from users.models import Profiles
# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(Profiles, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner=
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
