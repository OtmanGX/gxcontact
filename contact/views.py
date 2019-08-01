from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contact


# Create your views here.

def user_owner_required(Cls):
    class View(Cls):
        def __init__(self, *args, **kwargs):
            super(*args, **kwargs)

        def get(self, request, *args, **kwargs):
            if not self.get_object().created_by == self.request.user:
                return HttpResponseForbidden(render(request, "forbidden.html", {}))
            else:
                return super().get(request, *args, **kwargs)
    return View


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'contact.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(created_by=self.request.user)


@user_owner_required
class DetailPageView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'


@login_required
def search_contact(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(info__icontains=search_term) |
            Q(number__icontains=search_term)
        )
        context = {
            'search_term': search_term,
            'contacts': search_results.filter(created_by=request.user)
        }
        return render(request, 'search.html', context)
    else:
        redirect('home')


class ContactCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Contact
    fields = ['name', 'email', 'number', 'gender', 'info', 'image']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        instance.save()
        messages.success(self.request, "Contact has been successfully created")
        return redirect('home')


@user_owner_required
class ContactUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    model = Contact
    fields = ['name', 'email', 'number', 'gender', 'info', 'image']

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, "Contact has been successfully updated")
        return redirect('show_contact', instance.pk)


@user_owner_required
class ContactDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Contact
    success_url = "/"
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Contact has been successfully deleted")
        return super().delete(self, request, *args, **kwargs)
