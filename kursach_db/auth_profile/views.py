from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import ProfileForm
from django.contrib.auth import authenticate, login, logout

from .models import Profile


class LoginAuthView(LoginView):
    template_name = "auth.html"

    def get_success_url(self):
        return reverse("auth:profile")


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "login_register.html"
    success_url = reverse_lazy("auth:profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("auth:login")


class AboutMeUpdateView(TemplateView):
    template_name = "auth_profile.html"

    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return self.render_to_response({'form': form})

    def post(self, request: HttpRequest):
        form = ProfileForm(request.POST, request.FILES, instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            form.instance.user_id = request.user
            profile_update = Profile.objects.get(user_id=request.user.id)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            age = str(request.POST['age'])
            passport = request.POST['passport']
            passport_region = request.POST['passport_region']
            study_type = request.POST['study_type']
            study_place = request.POST['study_place']
            try:
                file = request.FILES['picture']
                profile_update.picture.delete()
                profile_update.picture = file
            except:
                pass
            profile_update.last_name = last_name
            profile_update.first_name = first_name
            profile_update.age = age
            profile_update.passport = passport
            profile_update.passport_region = passport_region
            profile_update.study_type = study_type
            profile_update.study_place = study_place
            # profile_update.save()
            form.save()
            return redirect(request.path)


class AboutMeView(TemplateView):
    template_name = "about_me.html"
