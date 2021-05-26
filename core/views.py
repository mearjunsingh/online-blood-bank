from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.paginator import Paginator
from . import forms
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, 'index.html')


def search_page(request):
    if 'blood' in request.GET and 'district' in request.GET and 'local' in request.GET:
        blood = request.GET.get('blood')
        district = request.GET.get('district')
        local = request.GET.get('local')
        b_url = '?blood=' + blood + '&district=' + district + '&local=' + local + '&'
        post_list = User.objects.filter(is_donor=True).filter(blood_group__iexact=blood).filter(district__iexact=district).filter(local_level__iexact=local).order_by('-last_login')
    else:
        b_url = '?'
        post_list = User.objects.filter(is_donor=True).order_by('-last_login')
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
        return render(request, 'donors-listing-page.html', {'users' : users, 'base_url' : b_url})
    else:
        return render(request, 'donors-listing-page.html')


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