from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import LoginForm, RegisterForm, ChangePasswordForm, UserChangeForm, PhotoForm
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from core.models import Request


def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = LoginForm(request=request, data=request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_cre = authenticate(email=email, password=password)
            login(request, user_cre)
            if 'next' in request.POST:
                next_url = request.POST.get('next')
                return redirect(next_url)
            else:
                return redirect('home_page')
        return render(request, 'login.html', {'form' : form})


def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard_page')
    else:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            if obj.id == 1:
                obj.is_staff = True
                obj.is_superuser = True
                obj.save()
            return redirect('login_page')
        return render(request, 'register.html', {'form': form})


def logout_page(request):
    if not request.user.is_authenticated:
        raise Http404()
    else:
        logout(request)
        return redirect('home_page')


@login_required()
def dashboard_page(request):
    donated = Request.objects.filter(donated_by=request.user).filter(status='completed').order_by('for_date')
    pendings = Request.objects.filter(donated_by=request.user).exclude(status='completed').exclude(status='canceled').order_by('for_date')
    instance = get_object_or_404(User, email=request.user.email)
    form = UserChangeForm(request.POST or None, instance=instance)
    photo_form = PhotoForm()
    if form.is_valid():
        form.save()
        return redirect('dashboard_page')
    context = {
        'photo_form' : photo_form,
        'form' : form,
        'donated' : donated,
        'pendings' : pendings
    }
    return render(request, 'dashboard.html', context)


@login_required()
def manage_request_page(request):
    ongoing_requests = Request.objects.filter(requested_by=request.user).exclude(
        Q(status = 'completed') | 
        Q(status = 'canceled')
    ).order_by('for_date')
    completed_requests = Request.objects.filter(requested_by=request.user).filter(
        Q(status = 'completed') | 
        Q(status = 'canceled')
    ).order_by('-for_date')
    return render(request, 'requests.html', {'ongoing_requests' : ongoing_requests, 'completed_requests' : completed_requests})


@login_required()
def changePassword_page(request):
    form = ChangePasswordForm(user=request.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect('dashboard_page')
    return render(request, 'change-password.html', {'form' : form})


def upload_image(request):
    instance = get_object_or_404(User, email=request.user.email)
    image = PhotoForm(data=request.POST, files=request.FILES, instance=instance)
    if image.is_valid():
        image.save()
    return redirect('dashboard_page')