from django.shortcuts import render
# from allauth.app_settings import USER_MODEL
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html")


def profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    context = {
        "user": user,
    }

    return render(request, "home.html", context)
