from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404
from django.contrib.auth import get_user_model
User = get_user_model()


def change_is_donor(request):
    if request.method == 'POST':
        try:
            user = get_object_or_404(User, id=request.user.id)
            user.is_donor = not user.is_donor
            user.save()
            data = {
                'result' : True
            }
        except:
            data = {
                'result' : False
            }
        return JsonResponse(data)
    else:
        raise Http404()