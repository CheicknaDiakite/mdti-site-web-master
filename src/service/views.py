from django.shortcuts import render, get_object_or_404

from service.models import Service


# Create your views here.


def service_index(request):

    list_services = Service.objects.all()
    context = {"list_services": list_services}

    return render(request, "service/service_index.html", context)

def service_detail(request, slug):

    list_service = get_object_or_404(Service, slug = slug)
    context = {"service": list_service}

    return render(request, "service/service_detail.html", context)