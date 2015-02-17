from django.shortcuts import render
from django.contrib.auth.models import User
from actstream.models import actor_stream

def user_timeline(request, username):
    user = User.objects.get(username=username)
    user_actions = actor_stream(user)
    context = {
        'user': user,
        'activities': user_actions,
    }
    return render(request, 'timeline.html', context)
