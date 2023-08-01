from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as UserModel
from django.contrib.auth.decorators import login_required

from . import forms
from . import models
from . import mixins


# Certs
class Certs(ListView):
    model = models.Cert
    template_name = "portfolio/certs.html"


class CertCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Cert
    form_class = forms.CertForm
    template_name = "portfolio/cert_create_form.html"


class CertDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Cert
    template_name = "portfolio/cert_delete_form.html"
    success_url = "/certs"


class CertUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Cert
    form_class = forms.CertForm
    template_name = "portfolio/cert_update_form.html"
    success_url = "/certs"


# Code
class Code(ListView):
    model = models.Code
    template_name = "portfolio/code.html"


class CodeCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Code
    form_class = forms.CodeForm
    template_name = "portfolio/code_create_form.html"


class CodeDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Code
    form_class = forms.CodeForm
    template_name = "portfolio/code_delete_form.html"
    success_url = '/code'


class CodeUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Code
    form_class = forms.CodeForm
    template_name = "portfolio/code_update_form.html"
    success_url = '/code'


# Exp
class Exp(ListView):
    model = models.Exp
    template_name = 'portfolio/exp.html'


class ExpCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Exp
    form_class = forms.ExpForm
    template_name = 'portfolio/exp_create_form.html'
    success_url = '/exp'


class ExpDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Exp
    form_class = forms.ExpForm
    template_name = 'portfolio/exp_delete_form.html'
    success_url = '/exp'


class ExpUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Exp
    form_class = forms.ExpForm
    template_name = 'portfolio/exp_update_form.html'
    success_url = '/exp'


# Skills
class Skills(ListView):
    model = models.Skill
    template_name = "portfolio/skills.html"


class SkillCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Skill
    form_class = forms.SkillForm
    template_name = "portfolio/skill_create_form.html"
    success_url = "/skills"


class SkillDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Skill
    form_class = forms.SkillForm
    template_name = "portfolio/skill_delete_form.html"
    success_url = "/skills"


class SkillUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Skill
    form_class = forms.SkillForm
    template_name = "portfolio/skill_update_form.html"
    success_url = "/skills"


# Home
class Home(TemplateView):
    template_name = "portfolio/index.html"


# User/Login
class UserCreate(CreateView):
    model = UserModel
    form_class = forms.UserCreateForm
    template_name = 'portfolio/signup.html'

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next:
            return reverse_lazy('portfolio:login')+f"?next={next}"
        return reverse_lazy('portfolio:login')


@login_required
def auth_logout(request):
    logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    return redirect(reverse_lazy("portfolio:home"))
