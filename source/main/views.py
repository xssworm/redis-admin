from django.shortcuts import render_to_response, RequestContext
from django.utils.translation import ugettext as _

def draw_dashboard(request):
	return render_to_response('dashboard.html', {},
										  context_instance=RequestContext(request))