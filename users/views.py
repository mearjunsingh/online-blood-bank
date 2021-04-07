from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.paginator import Paginator
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    user = User.objects.get(email='bibekmoktan1222@gmail.com')
    return render(request, 'index.html', {'user' : user })


def search_page(request):
    if 'blood' and 'district' and 'local' in request.GET:
        blood = request.GET.get('blood')
        district = request.GET.get('district')
        local = request.GET.get('local')
        b_url = '?blood=' + blood + '&district=' + district + '&local=' + local + '&'
        post_list = User.objects.filter(is_donor=True).filter(blood_group__iexact=blood).filter(district__iexact=district).filter(local_level__iexact=local).order_by('-last_login')
    else:
        b_url = '?'
        post_list = User.objects.all().order_by('-last_login')
    if post_list.count() != 0:
        paginator = Paginator(post_list, 10)
        if 'page' in request.GET:
            q = request.GET['page']
            if q is not None and q != '' and q != '0':
                page_number = request.GET.get('page')
            else:
                page_number = 1
        else:
            page_number = 1
        users = paginator.get_page(page_number)
        return render(request, 'result.html', {'users' : users, 'base_url' : b_url})
    else:
        return render(request, 'result.html')
    return render(request, 'result.html')


def user_page(request):
    return render(request, 'profile.html')

# finished
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

# finished
def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard_page')
    else:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})


@login_required()
def dashboard_page(request):
    return render(request, 'dashboard.html')