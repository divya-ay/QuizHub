from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class CustomAuthForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Wrong username or password. Please try again.",
        "inactive": "This account is inactive.",
    }

class CustomLoginView(LoginView):
    form_class = CustomAuthForm
    template_name = "userauth/login.html"
    redirect_authenticated_user = True

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({
                "class": "form-control form-control-lg",
                "placeholder": field.label,
            })
        return form

class CustomSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Confirm Password",
        }

class SignUpView(CreateView):
    form_class = CustomSignUpForm
    template_name = "userauth/signup.html"
    success_url = reverse_lazy("userauth:login")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({
                "class": "form-control form-control-lg",
                "placeholder": field.label,
            })
        return form

    def form_valid(self, form):
        return super().form_valid(form)