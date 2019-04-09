from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
from django.shortcuts import render


# Create your views here.
def index(request):
    all_tutorials = Tutorial.objects.all()
    context = {
        'tutorials': all_tutorials
    }

    return render(request, "tutorials/index.html", context)


def see_tutorial(request, tutorial_id):
    try:
        tutorial = Tutorial.objects.get(pk=tutorial_id)
    except Tutorial.DoesNotExist:
        return HttpResponse("Page not found. Sorry!")

    context = {
        'tutorial': tutorial
    }

    # Even when saving data we can use Django's API
    tutorial.num_views += 1
    tutorial.save()

    return render(request, "tutorials/tutorial.html", context)
