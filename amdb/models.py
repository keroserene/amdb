from django.db import models

class Domain(models.Model):
  name = models.CharField(max_length=32)
  description = models.CharField(max_length=256)


class _AMDB_Obj(models.Model):

class Observation(_AMDB_Obj):
  blob = models.Whatever()
  description = models.CharFlied(max_length=256)

  def __unicode__(self):
    return self.description

class Assertion(_AMDB_Obj):
  basis = models.ForeignKey(Observation)
  domain = models.ForeignKey(Domain)

class Implication(Assertion):
  derivation = models.ManyToManyField(Assertion)


class Action(_AMDB_Obj):
  pass

class Capability(_AMDB_Obj):
  derivation = models.ManyToManyField(Assertion)
  action = models.ForeignKey(Action)
