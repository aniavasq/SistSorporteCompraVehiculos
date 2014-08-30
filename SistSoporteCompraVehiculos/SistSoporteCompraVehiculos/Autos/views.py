from django.shortcuts import render_to_response
from django.forms.models import ModelForm
from django.template.context import RequestContext
from django.http import Http404

from SistSoporteCompraVehiculos.Autos.models import Automotor

from Util.ResponseMethod import ResponseMethod

def add_car(request):
    print str(request.method)
    response_method = ResponseMethod(Automotor)
    
    def post_action(request):
        auto_form = AutoForm(request.POST)
        if auto_form.is_valid():
            auto_form.save(commit=True)
        return auto_form
    
    def get_action(request):
        return AutoForm()
    
    form = response_method.do_on_request(request, {'POST': post_action, 'GET': get_action})
    return render_to_response('form_add_auto.html', {'form': form}, context_instance = RequestContext(request))

def get_cars(request):
    cars = []
    if 'id' in request.GET.keys():
        id_auto = request.GET['id']
        if id_auto:
            try:
                cars = [Automotor.objects.get(id_auto=id_auto)]
            except:
                raise Http404
    else:
        cars = Automotor.objects.all()
    return render_to_response('get_cars.html', {'cars': cars}, context_instance = RequestContext(request))       

class AutoForm(ModelForm):
    class Meta:
        model = Automotor