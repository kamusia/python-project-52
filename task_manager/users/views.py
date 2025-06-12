from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import User
from .forms import UserCreateForm, UserLoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect


class UserOwnerMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = reverse_lazy('login')
    error_message_auth = 'Вы не авторизованы! Пожалуйста, выполните вход.'
    error_message_permission = 'У вас нет прав для изменения другого пользователя.'

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.error_message_auth)
            return redirect('login')
        messages.error(self.request, self.error_message_permission)
        return redirect('users:list')


class HomePageView(TemplateView):
    template_name = 'home.html'


class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно создан'


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_message = 'Вы залогинены'


class UserLogoutView(SuccessMessageMixin, LogoutView):
    success_message = 'Вы разлогинены'


class UserUpdateView(UserOwnerMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')
    success_message = 'Пользователь успешно изменен'


class UserDeleteView(UserOwnerMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')
    success_message = 'Пользователь успешно удален'
