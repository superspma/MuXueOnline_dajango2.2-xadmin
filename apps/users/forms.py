import redis
from django import forms
from captcha.fields import CaptchaField

from MxOnline.settings import REDIS_HOST, REDIS_PORT


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses='utf8')
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码错误！')
        return self.cleaned_data

    # def clean(self):
    #     mobile = self.cleaned_data['mobile']
    #     code = self.cleaned_data['code']
    #     r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses='utf8')
    #     redis_code = r.get(str(mobile))
    #     if code != redis_code:
    #         raise forms.ValidationError('验证码错误！')
    #     return self.cleaned_data
