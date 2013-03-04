from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
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
  # List of all lists.
  obs_list = Observation.objects.all()
  ass_list = Assertion.objects.all()
  cap_list = Capability.objects.all()
  obs_list.cls = 'observation'
  ass_list.cls = 'assertion'
  cap_list.cls = 'capability'
  obs_list.cls_plural = 'observations'
  ass_list.cls_plural = 'assertions'
  cap_list.cls_plural = 'capabilities'
  obj_lists = [
      obs_list,
      ass_list,
      cap_list,
  ]
  context = {
      'view_mode': mode,
      'obj_lists': obj_lists,
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
        return redirect('/')
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

def new(request, cls): return edit(request, cls, '0')

def imply(request, assertion_id):
  return HttpResponse('creating implication from assertion: %s' % assertion_id)

def nuke(request):
  return HttpResponse('are you sure? :( ')

def nuke_fo_realz(request):
  Observation.objects.all().delete()
  Assertion.objects.all().delete()
  Capability.objects.all().delete()
  return index(request)

#render_to_response(
#      'index.html', {}, 
#      context_instance=RequestContext(request))
#

#@register.assignment_tag
#def set_var(x):
#  return x
