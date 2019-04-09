from django.shortcuts import render
from .models import Thread, Response
from django.http import HttpResponse


# Create your views here.
def index(request):
    all_threads = Thread.objects.all()
    context = {
        'threads': all_threads
    }
    return render(request, 'forum/index.html', context)


def see_thread(request, thread_id):
    try:
        thread = Thread.objects.get(pk=thread_id)
    except Thread.DoesNotExist:
        return HttpResponse("Page not found. Sorry!")

    context = {
        'thread': thread
    }

    return render(request, 'forum/thread.html', context)
