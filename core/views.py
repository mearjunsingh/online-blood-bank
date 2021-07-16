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
    if user.is_donor:
        form = forms.RequestUser(request.POST or None, request.FILES or None)
        msg = None
        if form.is_valid():
            if request.user.is_authenticated and (user != request.user):
                obj = form.save(commit=False)
                obj.requested_by = request.user
                obj.donated_by = user
                obj.blood_group = user.blood_group
                obj.save()
                form = forms.RequestUser()
                msg = 'Successfully submitted.'
            else:
                msg = 'You must login to send request.'
        return render(request, 'profile.html', {'user' : user, 'form': form, 'msg': msg})
    else:
        msg = 'Donor unavailable at the moment.'
        return render(request, 'profile.html', {'user' : user, 'msg': msg})


def search_page(request):
    user_list = User.objects.filter(is_donor=True).filter(is_active=True).exclude(id=request.user.id).order_by('-last_login')
    b_url = '?'
    blood = None
    if 'blood' in request.GET:
        blood = request.GET.get('blood')
        if blood is not None and blood != '':
            blood = get_object_or_404(Blood, slug=blood)
            user_list = user_list.filter(blood_group=blood)
            b_url += f'blood={blood.slug}&'
    if 'district' in request.GET:
        district = request.GET.get('district')
        if district is not None and district != '':
            user_list = user_list.filter(district__iexact=district)
            b_url += f'district={district}&'
    if 'local' in request.GET:
        local = request.GET.get('local')
        if local is not None and local != '':
            user_list = user_list.filter(local_level__iexact=local)
            b_url = f'local={local}&'

    if user_list.count() != 0:
        paginator = Paginator(user_list, 20)
        if 'page' in request.GET:
            page = request.GET['page']
            if page is not None and page != '' and page != '0':
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
    form = forms.RequestForm(data=request.POST or None, files=request.FILES or None)
    msg = None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.requested_by = request.user
        obj.save()
        form = forms.RequestForm()
        msg = 'Successfully Submitted.'
    return render(request, 'submit-request.html', {'form': form, 'msg': msg})


def pending_requests(request):
    blood_requests = Request.objects.filter(donated_by=None).filter(status='pending').order_by('for_date')
    return render(request, 'pending-requests.html', {'blood_requests' : blood_requests})


@login_required()
def offer_help(request, id):
    blood_request = get_object_or_404(Request, id=id, status='pending', donated_by=None)
    if blood_request.requested_by != request.user:
        blood_request.donated_by = request.user
        blood_request.status = 'verified'
        blood_request.save()
    return redirect('pending_requests')


@login_required()
def verify_request_status(request, id):
    blood_request = get_object_or_404(Request, id=id, donated_by=request.user, status='pending')
    if blood_request.requested_by != request.user:
        blood_request.status = 'verified'
        blood_request.save()
    return redirect('dashboard_page')


@login_required()
def deny_request_status(request, id):
    blood_request = get_object_or_404(Request, id=id, donated_by=request.user, status='pending')
    if blood_request.requested_by != request.user:
        blood_request.donated_by = None
        blood_request.save()
    return redirect('dashboard_page')


@login_required()
def complete_request_status(request, id):
    blood_request = get_object_or_404(Request, id=id, requested_by=request.user, status='verified')
    if blood_request.donated_by != request.user:
        blood_request.status = 'completed'
        blood_request.save()
    return redirect('manage_request_page')


@login_required()
def cancel_request_status(request, id):
    blood_request = get_object_or_404(Request, id=id, requested_by=request.user, status='pending')
    blood_request.status = 'canceled'
    blood_request.save()
    return redirect('manage_request_page')