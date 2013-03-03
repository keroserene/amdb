from django.template import RequestContext
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

def observation(request, observation_id):
  # obs = Observation.objects.get(pk=observation_id)
  obs = get_object_or_404(Observation, pk=observation_id)
  return render(request, 'amdb/observation.html', {'obs': obs})
  # return HttpResponse('viewing details for observation: %s' % observation_id)
 
def assertion(request, assertion_id):
  ass = get_object_or_404(Assertion, pk=assertion_id)
  return HttpResponse('viewing details for assertion: %s' % assertion_id)

def capability(request, capability_id):
  return HttpResponse('viewing details for capability: %s' % capability_id)

def imply(request, assertion_id):
  return HttpResponse('creating implication from assertion: %s' % assertion_id)

def edit(request, obj_id):
  pass
#render_to_response(
#      'index.html', {}, 
#      context_instance=RequestContext(request))
