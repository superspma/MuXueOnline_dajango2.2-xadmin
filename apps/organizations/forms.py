import re

from django import forms

from apps.operations.models import UserAsk


# class AddAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=10)
#     mobile = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=2, max_length=20)


class AddAskForm(forms.ModelForm):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        '''
        验证手机号码是否合法
        :return:
        '''
        mobile = self.cleaned_data['mobile']
        regex_mobile = '^((13[0-9])|(14[5,6,7,9])|(15[^4])|(16[5,6])|(17[0-9])|(18[0-9])|(19[1,8,9]))\\d{8}$'
        p = re.compile(regex_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法！', code='mobile_invalid')
