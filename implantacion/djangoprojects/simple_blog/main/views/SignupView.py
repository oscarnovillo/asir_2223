from django.shortcuts import render

from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# Forms
from main.forms import SignupForm


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'main/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('main:registerok')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)