from django.db import models
# from django_pgjson.fields import JsonField
from django.contrib.postgres.fields import JSONField as JsonField
# Create your models here.

class CompanyItem(models.Model):
    name = models.TextField(null=True)
    url = models.TextField(null=True)
    employees = JsonField(null=True)

class HunterItem(models.Model):
    name = models.TextField(null=True)
    email = models.TextField(null=True)
    pattern = models.TextField(null=True)
    sources = models.TextField(null=True)
    html = models.TextField(null=True)

class SourceItem(models.Model):
    url = models.TextField(null=True)
    emails = JsonField(null=True)
    links = JsonField(null=True)
    html = models.TextField(null=True)
    timestamp = models.TextField(null=True)


class HunterItemBaba(models.Model):
    url = models.TextField(null=True)
    data = models.JsonField(null=True)

class SourceItemBaba(models.Model):
    url = models.TextField(null=True)
    data = models.JsonField(null=True)