from django.shortcuts import render
from django.views import View
from pure_pagination import Paginator, PageNotAnInteger

from apps.courses.models import Course
from apps.operations.models import UserFavorite


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        """获取课程详情"""
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        # 获取收藏状态
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        return render(request, 'course-detail.html', {
            'course': course,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
        })


class CourseListView(View):
    def get(self, request, *args, **kwargs):
        '''获取课程列表信息'''
        all_courses = Course.objects.order_by('add_time')
        hot_course = Course.objects.order_by('-click_nums')[:3]
        # 排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_courses.order_by('-students')
        elif sort == 'hot':
            all_courses = all_courses.order_by('-click_nums')
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=9, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_course': hot_course,
        })
