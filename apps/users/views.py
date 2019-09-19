from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', locals())

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get('username', '')
        password = request.POST.get('password', '')

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
            return render(request, 'login.html', {'msg': '用户名或密码错误！'})
