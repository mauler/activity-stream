from actstream.actions import follow, unfollow, is_following
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from actstream.models import actor_stream, user_stream


def timeline(request):
    activities = user_stream(request.user)
    context = {
        'activities': activities,
    }
    return render(request, 'all_timeline.html', context)


def user_timeline(request, username):
    user = User.objects.select_related('profile').get(username=username)
    user_actions = []

    if is_following(request.user, user) or not user.profile.private:
        user_actions = actor_stream(user)

    context = {
        'user': user,
        'activities': user_actions,
    }
    return render(request, 'timeline.html', context)


def follow_user(request, username):
    follow(request.user, User.objects.get(username=username))
    return redirect('user_timeline', username)


def unfollow_user(request, username):
    unfollow(request.user, User.objects.get(username=username))
    return redirect('user_timeline', username)