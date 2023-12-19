"""
module docstring
"""
from django.contrib.auth.forms import AuthenticationForm

from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    error_messages = {
        'invalid_login':
            "نام کاربری یا کلمه عبور اشتباه است"
        ,
        'inactive':
            "این اکانت غیرفعال است",
    }

    class Meta:
        fields = ('username', 'password', 'captcha',)
