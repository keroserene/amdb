from django.db import models
from django import forms

class Domain(models.Model):
  """Potential Domain Types."""
  name = models.CharField(max_length=32)
  description = models.CharField(max_length=256)
  blob = models.CharField(max_length=128)

class _AMDB_Obj(models.Model):
  pass

class Observation(_AMDB_Obj):
  # blob = models.r()
  description = models.CharField(
      max_length=256)

  def __unicode__(self):
    return self.description

DOMAINS = [
  ('Syria', 'lol'),
  ('China', 'haha'),
]

class Assertion(_AMDB_Obj):
  basis = models.ForeignKey(Observation)
  description = models.CharField(max_length=256)
  domain = models.CharField(max_length=8, choices=DOMAINS)
  # domain = models.ForeignKey(Domain)

  def __unicode__(self):
    return '%s : %s' % (self.basis, self.description)

class Implication(Assertion):
  derivation = models.ManyToManyField(Assertion, related_name='d+')

class Action(_AMDB_Obj):
  pass

class Capability(_AMDB_Obj):
  derivation = models.ManyToManyField(Assertion)
  action = models.ForeignKey(Action)
