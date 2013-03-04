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

  def get_absolute_url(self):
    return '/observation/%i/' % self.id

DOMAINS = [
  ('Lulz', 'Internets'),
  ('Rawr', 'The Grue'),
]

class Assertion(_AMDB_Obj):
  description = models.CharField(max_length=256)
  basis = models.ForeignKey(
      Observation,
      help_text='Derivation frow observation(s).')
  domain = models.CharField(max_length=8, choices=DOMAINS)
  # domain = models.ForeignKey(Domain)

  def __unicode__(self):
    return '%s --> %s [%s]' % (self.basis, self.description, self.domain)

  def get_absolute_url(self):
    return '/assertion/%i/' % self.id


class Implication(Assertion):
  derivation = models.ManyToManyField(
      Assertion, related_name='d+',
      help_text='Derivation from Assertion(s) and Implication(s).')

  def get_absolute_url(self):
    return '/implication/%i/' % self.id

#class Action(_AMDB_Obj):
#  def __unicode__(self):
#    return 'Actor %s acts upon asset %s' ('[REDACTED]', '[REDACTED]')

class Capability(_AMDB_Obj):
  action = models.CharField(max_length=256)
  derivation = models.ManyToManyField(
      Assertion,
      help_text='Derivation from Assertion(s) and Implication(s).')
  # action = models.ForeignKey(Action)
  
  def __unicode__(self):
    return '%s (%s)' % (self.action, self.derivation.all())

  def get_absolute_url(self):
    return '/capability/%i/' % self.id
