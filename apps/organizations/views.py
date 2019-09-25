from django.shortcuts import render
from django.views.generic.base import View

from pure_pagination import Paginator, PageNotAnInteger
from django.http import JsonResponse
from apps.organizations.forms import AddAskForm
from apps.organizations.models import CourseOrg, City


class AddAskView(View):
    '''
    处理用户的需求
    '''

    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status": "success",
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "添加失败！"
            })


class OrgView(View):
    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据，展示到页面
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()

        # 授课机构排名
        hot_org = all_orgs.order_by('-click_nums')[:3]

        # 通过机构类别对课程机构进行筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 通过所在城市对课程机构进行筛选
        city_id = request.GET.get('city', '')
        if city_id and city_id.isdigit():
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 对授课机构进行排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-course_nums')

        org_counts = all_orgs.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, per_page=5, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html',
                      {'all_orgs': orgs,
                       'org_counts': org_counts,
                       'all_citys': all_citys,
                       'category': category,
                       'city_id': city_id,
                       'sort': sort,
                       'hot_org': hot_org
                       })
