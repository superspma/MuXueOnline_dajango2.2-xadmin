from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.organizations.models import CourseOrg, City


class OrgView(View):
    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据，展示到页面
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()

        # 通过机构类别对课程机构进行筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 通过所在城市对课程机构进行筛选
        city_id = request.GET.get('city', '')
        if city_id and city_id.isdigit():
            all_orgs = all_orgs.filter(city_id=int(city_id))

        org_counts = all_orgs.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, per_page=1, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html',
                      {'all_orgs': orgs,
                       'org_counts': org_counts,
                       'all_citys': all_citys,
                       'category': category,
                       'city_id': city_id,
                       })
