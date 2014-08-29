from django.conf.urls.defaults import patterns, url
import Autos.views as cars_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^addCar.html', cars_views.add_car),
                       url(r'^getCars.html', cars_views.get_cars),
    # Examples:
    # url(r'^$', 'SistSoporteCompraVehiculos.views.home', name='home'),
    # url(r'^SistSoporteCompraVehiculos/', include('SistSoporteCompraVehiculos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
