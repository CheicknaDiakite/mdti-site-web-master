from django.shortcuts import render

from presentation.models import Slider


# Create your views here.


def presentation_index(request):

    list_presentations = Slider.objects.all()
    context = {"list_presentations": list_presentations}

    return render(request,"presentation/presentation_index.html", context)