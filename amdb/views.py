from django import template
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404

from models import Observation, Assertion, Capability

def index(request):
  # List of latest things
  # obs_list = Observation.objects.all().order_by('id')[:5]
  obs_list = Observation.objects.all()
  ass_list = Assertion.objects.all()
  cap_list = Capability.objects.all()
  context = {
      'obs_list': obs_list,
      'ass_list': ass_list,
      'cap_list': cap_list,
  }
  return render(request, 'amdb/index.html', context)

def edit(request, edit_class, id):
  if 'observation' is edit_class:
    return observation(request, id, edit=True)
  return observation(request, id, edit=True)

def _AMDBcontext(obj_class, obj, edit):
  return {'obj_class': obj_class,
          'templ_path': 'amdb/%s.html' % obj_class,
          'obj': obj,
          'edit': edit}

def observation(request, observation_id, edit=False):
  obs = get_object_or_404(Observation, pk=observation_id)
  return render(request, 'amdb/details.html', _AMDBcontext('observation', obs, edit))
 
def assertion(request, assertion_id):
  ass = get_object_or_404(Assertion, pk=assertion_id)
  return render(request, 'amdb/details.html', _AMDBcontext('assertion', ass, edit))

def capability(request, capability_id):
  cap = get_object_or_404(Capability, pk=capability_id)
  return render(request, 'amdb/details.html', _AMDBcontext('capability', cap, edit))

def imply(request, assertion_id):
  return HttpResponse('creating implication from assertion: %s' % assertion_id)


def nuke(request):
  return HttpResponse('Asplodeded!')

#render_to_response(
#      'index.html', {}, 
#      context_instance=RequestContext(request))
#

#@register.assignment_tag
#def set_var(x):
#  return x
