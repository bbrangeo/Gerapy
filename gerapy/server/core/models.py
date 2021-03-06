from django.db import models

# Create your models here.
from django.db.models import Model, CharField, GenericIPAddressField, IntegerField, TextField, DateTimeField, \
    ManyToManyField, ForeignKey


class Client(Model):
    name = CharField(max_length=255, default=None)
    ip = GenericIPAddressField(max_length=255, default='')
    port = IntegerField(default=6800, blank=True)
    description = TextField(default='', blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Project(Model):
    name = CharField(max_length=255, default=None)
    description = CharField(max_length=255, default='', blank=True)
    egg = CharField(max_length=255, default='', blank=True)
    built_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    clients = ManyToManyField(Client, through='Deploy')


class Deploy(models.Model):
    client = ForeignKey(Client)
    project = ForeignKey(Project)
    description = CharField(max_length=255, default='', blank=True)
    deployed_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
