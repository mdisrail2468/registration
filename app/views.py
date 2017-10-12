from app.emails import render_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


@login_required
def root_view(request):
    if request.user.has_perm('register.vote'):
        return HttpResponseRedirect(reverse('vote'))
    elif request.user.has_perm('checkin.check_in'):
        return HttpResponseRedirect(reverse('check_in_list'))
    try:
        request.user.hacker
        return HttpResponseRedirect(reverse('dashboard'))
    except:
        return HttpResponseRedirect(reverse('profile'))


@login_required
def view_email(request):
    msg = render_mail('test_email/test', ['test@hackupc.com'],
                      {'subject': 'TEST', 'fb': 'hackupc'})
    return HttpResponse(msg.body)
