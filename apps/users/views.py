from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.forms import LoginForm


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'login.html', locals())

    def post(self, request, *args, **kwargs):
        # 表单验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            # if not user_name:
            #     return render(request, 'login.html', {'msg': '请输入用户名！'})
            # if not password:
            #     return render(request, 'login.html', {'msg': '请输入密码！'})
            # if len(password) < 3:
            #     return render(request, 'login.html', {'msg': '密码格式错误！'})

            # 通过用户名和密码查询用户是否存在
            user = authenticate(username=user_name, password=password)
            # from apps.users.models import UserProfile
            # 1通过用户名查询用户 （不推荐）
            # 2需要先加密在通过加密后的密码查询用户名密码是否匹配
            # user=UserProfile.objects.get(username=user_name,password=password)

            # 用于查询用户是否存在
            if user is not None:
                # 查询到用户
                login(request, user)
                # 登陆成功之后，如何返回页面
                return HttpResponseRedirect(reverse('index'))
            else:
                # 未查询到用户
                return render(request, 'login.html', {'msg': '用户名或密码错误！', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})
