from core.models import Blood, Request
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.paginator import Paginator
from . import forms
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, 'index.html')


def user_page(request, id):
    user = get_object_or_404(User, id=id)
    if user == request.user:
        return redirect('dashboard_page')
    form = forms.RequestUser(request.POST or None)
    msg = None
    if form.is_valid():
        if request.user.is_authenticated and (user != request.user):
            obj = form.save(commit=False)
            obj.requested_by = request.user
            obj.donated_by = user
            obj.blood_group = user.blood_group
            obj.save()
            msg = 'Successfull Submitted.'
        else:
            msg = 'You Must Login to Send Request.'
    return render(request, 'profile.html', {'user' : user, 'form': form, 'msg': msg})


def search_page(request):
    if 'blood' in request.GET and 'district' in request.GET and 'local' in request.GET:
        blood = request.GET.get('blood')
        blood = get_object_or_404(Blood, slug=blood) #Blood.objects.get(slug=blood)
        district = request.GET.get('district')
        local = request.GET.get('local')
        b_url = '?blood=' + blood.slug + '&district=' + district + '&local=' + local + '&'
        post_list = User.objects.filter(is_donor=True).filter(blood_group=blood).filter(district__iexact=district).filter(local_level__iexact=local).exclude(id=request.user.id).order_by('-last_login')
    else:
        blood = None
        b_url = '?'
        post_list = User.objects.filter(is_donor=True).exclude(id=request.user.id).order_by('-last_login')
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
        return render(request, 'donors-listing-page.html', {'users' : users, 'base_url' : b_url, 'blood' : blood})
    else:
        return render(request, 'donors-listing-page.html', {'blood' : blood})


@login_required()
def submit_request(request):
    form = forms.RequestForm(request.POST or None)
    msg = None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.requested_by = request.user
        obj.save()
        msg = 'Successfull Submitted.'
    return render(request, 'submit-request.html', {'form': form, 'msg': msg})


def pending_requests(request):
    blood_requests = Request.objects.filter(status='pending').order_by('for_date')
    return render(request, 'pending-requests.html', {'blood_requests' : blood_requests})


@login_required()
def offer_help(request, id):
    blood_request = get_object_or_404(Request, id=id, status='pending')
    if blood_request.requested_by != request.user:
        blood_request.donated_by = request.user
        blood_request.status = 'verified'
        blood_request.save()
    return redirect('pending_requests')