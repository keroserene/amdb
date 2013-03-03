from django.template import RequestContext
from django.shortcuts import render, render_to_response

from models import Observation

def index(request):
  # List of latest things
  obs_list = Observation.objects.all().order_by('id')[:5]
  context = {'obs_list': obs_list}
  return render(request, 'amdb/index.html', context)

def observation(request, observation_id):
  return HttpResponse('viewing details for observation: %s' % observation_id)
 
def view_assertion(request, assertion_id):
  return HttpResponse('viewing details for assertion: %s' % assertion_id)

def view_capability(request, capability_id):
  return HttpResponse('viewing details for capability: %s' % assertion_id)

def imply(request, assertion_id):
  return HttpResponse('creating implication from assertion: %s' % assertion_id)

#render_to_response(
#      'index.html', {}, 
#      context_instance=RequestContext(request))
