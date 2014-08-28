from django.shortcuts import render_to_response
from django.forms.models import ModelForm
from SistSoporteCompraVehiculos.Autos.models import Automotor
from Util.ResponseMethod import ResponseMethod
from django.template.context import RequestContext

def add_car(request):
    response_method = ResponseMethod(Automotor)
    
    def post_action(request):
        return AutoForm(request.POST)
    
    def get_action(request):
        return AutoForm()
    
    form = response_method.do_on_request(request, {'POST': post_action, 'GET': get_action})
    return render_to_response('form_add_auto.html', {'form': form}, context_instance = RequestContext(request))

class AutoForm(ModelForm):
    class Meta:
        model = Automotor