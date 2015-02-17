from django.shortcuts import render


def user_timeline(request, username):
    return render(request, 'timeline.html')
