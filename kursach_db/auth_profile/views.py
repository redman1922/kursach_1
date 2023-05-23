from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import MyUserCreationForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Profile


def register_page(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'login_register.html', {'form': form})


class UserProfile(TemplateView):
    template_name = "auth_profile.html"

    def get_context_data(self, **kwargs):

        data = {}
        if self.request.user.is_authenticated:
            data['username'] = self.request.user.username
            data['email'] = self.request.user.email
            data['first_name'] = self.request.user.first_name
            data['last_name'] = self.request.user.last_name
            if hasattr(self.request.user, 'profile'):
                data['age'] = self.request.user.profile.age
                if self.request.user.profile.picture:
                    data['picture'] = self.request.user.profile.picture
                data['passport'] = self.request.user.profile.passport
                data['passport_region'] = self.request.user.profile.passport_region
                data['study_type'] = self.request.user.profile.study_type
                data['study_place'] = self.request.user.profile.study_place
                data['reg_date'] = self.request.user.profile.reg_date
                if self.request.user.profile.registrar:
                    data['registrar'] = self.request.user.profile.registrar
                data['comment'] = self.request.user.profile.comment

            form = EditProfileForm(data)
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return context

    def post(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        username = f' {self.request.user.username}'

        form = EditProfileForm(request.POST, request.FILES)

        context['form'] = form

        if request.user.is_authenticated:

            if form.is_valid():
                username = form.cleaned_data.get('username')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                passport = form.cleaned_data.get('passport')
                passport_region = form.cleaned_data.get('passport_region')
                study_type = form.cleaned_data.get('study_type')
                study_place = form.cleaned_data.get('study_place')
                experience = form.cleaned_data.get('experience')

                user_update = User.objects.get(id=request.user.id)
                user_update.username = username
                user_update.first_name = first_name
                user_update.last_name = last_name
                user_update.save()

                try:
                    profile_update: Profile = Profile.objects.get(user_id=request.user.id)
                except ObjectDoesNotExist:
                    profile_update = Profile.objects.create(
                        user=request.user,
                        passport=passport,
                        passport_region=passport_region,
                        study_type=study_type,
                        study_place=study_place,
                        experience=experience,
                    )

                profile_update.passport = passport
                profile_update.passport_region = passport_region
                profile_update.study_type = study_type
                profile_update.study_place = study_place
                profile_update.experience = experience

                profile_update.picture.delete()
                profile_update.picture = request.FILES['picture']
                profile_update.save()

                context['msg_theme'] = 'success'

            return self.render_to_response(context=context)


class LoginAuthView(LoginView):
    template_name = "auth.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "login_register.html"
    success_url = reverse_lazy("home")

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
    next_page = reverse_lazy("login")
