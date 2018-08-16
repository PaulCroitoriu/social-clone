from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic

from groups.models import Group, GroupMember
from . import forms

class SingleGroup(generic.DetailView):
    model = Group


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    model = Group
    form_class = forms.GroupForm


class ListGroup(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already member of the {} group".format(group.name)))

        else:
            messages.success(self.request, "You are now a member of {} group".format(group.name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug":self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:
            membership = GroupMember.objects.filter(
                            user=self.request.user,
                            group__slug=self.kwargs.get('slug')).get()

        except GroupMember.DoesNotExist:
            messages.warning(self.request, "You cannot leave this grup because you are not a member of it.")

        else:
            membership.delete()
            messages.success(self.request, "You have successfuly left this group")

        return super().get(request, *args, **kwargs)
