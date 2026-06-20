from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

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