from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django import forms

from models import Observation, Assertion, Capability

class ObservationForm(forms.ModelForm):
  class Meta: model = Observation
class AssertionForm(forms.ModelForm):
  class Meta: model = Assertion
class CapabilityForm(forms.ModelForm):
  class Meta: model = Capability
VALID_CLASSES = ['observation', 'assertion', 'capability']
S2CLASS = {
  'observation': Observation, 'assertion': Assertion, 'capability': Capability}
S2FORM = {
  'observation': ObservationForm, 'assertion': AssertionForm, 'capability': CapabilityForm}


def index(request, mode='list'):
  # List of latest things
  # obs_list = Observation.objects.all().order_by('id')[:5]
  obs_list = Observation.objects.all()
  ass_list = Assertion.objects.all()
  cap_list = Capability.objects.all()
  context = {
      'view_mode': mode,
      'obs_list': obs_list,
      'ass_list': ass_list,
      'cap_list': cap_list,
  }
  return render(request, 'amdb/index.html', context)

def _AMDBcontext(obj_class, obj, edit):
  return {'obj_class': obj_class,
          'templ_path': 'amdb/%s.html' % obj_class,
          'obj': obj,
          'edit': edit}

def examine(request, cls, id, edit=False):
  """Generic data examination view."""
  # Fetch the object if it exists. '0' is reserved for creating new elements.
  obj = None if '0' == id else get_object_or_404(S2CLASS[cls], pk=id)
  objform = S2FORM[cls]
  if edit:
    if 'POST' == request.method:
      edit = objform(request.POST, instance=obj)
      if edit.is_valid():
        edit.save()
        return index(request)
    else:
      edit = objform(instance=obj)
  return render(
      request, 'amdb/examine.html',
      {'obj_class': cls, 'templ_path': 'amdb/%s.html' % cls,
       'obj': obj, 'edit': edit})


def edit(request, cls, id):
  """Generic data editing view."""
  if cls not in VALID_CLASSES:
    raise Http404
  return examine(request, cls, id, edit=True)

def new(request, cls): return edit(request, cls, 0)


def imply(request, assertion_id):
  return HttpResponse('creating implication from assertion: %s' % assertion_id)

def nuke(request):
  Observation.objects.all().delete()
  return HttpResponse('Asplodeded!')

#render_to_response(
#      'index.html', {}, 
#      context_instance=RequestContext(request))
#

#@register.assignment_tag
#def set_var(x):
#  return x
