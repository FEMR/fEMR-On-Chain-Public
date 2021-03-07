import os

from django.core.mail import EmailMessage

from django.shortcuts import render, redirect, get_object_or_404


from .forms import SupportTicketForm, CommentForm
from .models import SupportTicket, Comment


def not_logged_in(request):
    return render(request, 'appMR/not_logged_in.html')


def __get_dev(request):
    if request.user.groups.filter(name='Developer').exists():
        bug_list = SupportTicket.objects.filter(active=True)
        done_list = SupportTicket.objects.filter(active=False)
        dev = True
    else:
        bug_list = SupportTicket.objects.filter(reporter=request.user).filter(active=True)
        done_list = SupportTicket.objects.filter(reporter=request.user).filter(active=False)
        dev = False
    return dev, bug_list, done_list


def new_bug_view(request, ticket_type=0):
    if request.user.is_authenticated:
        ticket_type = 0 if ticket_type == 1 else 1
        dev, bug_list, done_list = __get_dev(request)
        if request.method == 'POST':
            form = SupportTicketForm(request.POST)
            if form.is_valid():
                t = form.save()
                t.reporter = request.user
                t.status = '1'
                t.active = True
                t.save()
                form = SupportTicketForm()
            return render(request, 'appMR/bug_list.html', {'open': ticket_type, 'bug_list': bug_list, 'done_list': done_list, 'dev': dev, 'form': form})
        else:
            form = SupportTicketForm()
        return render(request, 'appMR/bug_list.html', {'open': ticket_type, 'bug_list': bug_list, 'done_list': done_list, 'dev': dev, 'form': form})
    else:
        return redirect('appMR:not_logged_in')


def bug_list_view(request, ticket_type=0):
    if request.user.is_authenticated:
        ticket_type = 0 if ticket_type == 1 else 1
        form = SupportTicketForm()
        dev, bug_list, done_list = __get_dev(request)
        return render(request, 'appMR/bug_list.html', {'open': ticket_type, 'bug_list': bug_list, 'done_list': done_list, 'dev': dev, 'form': form})
    else:
        return redirect('appMR:not_logged_in')


def bug_detail_view(request, id=None):
    if request.user.is_authenticated:
        m = get_object_or_404(SupportTicket, pk=id)
        comments = m.comments.all()
        comment_form = CommentForm()
        if request.user.groups.filter(name='Developer').exists():
            dev = True
        else:
            dev = False
        if request.method == 'POST':
            form = SupportTicketForm(request.POST or None, instance=m)
            if form.is_valid():
                t = form.save()
                if t.status == '6':
                    t.active = False
                else:
                    t.active = True
                t.save()
        else:
            form = SupportTicketForm(instance=m)
        return render(request, 'appMR/bug_detail.html', {'bug_id': m.id, 'dev': dev, 'form': form, 'comment_form': comment_form, 'comments': comments})
    else:
        return redirect('appMR:not_logged_in')


def post_comment_view(request, bug_id=None):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Developer').exists():
            dev = True
        else:
            dev = False
        m = get_object_or_404(SupportTicket, pk=bug_id)
        form = SupportTicketForm(instance=m)
        comment_form = CommentForm()
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                t = comment_form.save()
                t.author = request.user
                t.save()
                m.comments.add(t)
                m.save()
                EmailMessage(
                    "Response on AppMR Ticket {0}".format(bug_id),
                    t.comment,
                    [m.reporter.email],
                    reply_to=[os.environ.get('DEFAULT_FROM_EMAIL')]).send()
        comments = m.comments.all()
        return render(request, 'appMR/bug_detail.html', {'bug_id': m.id, 'dev': dev, 'form': form, 'comment_form': comment_form, 'comments': comments})
    else:
        return redirect('appMR:not_logged_in')