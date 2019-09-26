from django.http import JsonResponse

from django.views import View

from apps.courses.models import Course
from apps.operations.forms import UserFavoriteForm
from apps.operations.models import UserFavorite
from apps.organizations.models import CourseOrg, Teacher


class AddFavView(View):

    def post(self, request, *args, **kwargs):
        """处理用户收藏，取消收藏"""
        # 判断用户是否登录
        if not request.user.is_authenticated:
            return JsonResponse({
                'status': 'file',
                'msg': '用户未登录'
            })

        user_fav_form = UserFavoriteForm(request.POST)
        if user_fav_form.is_valid():
            fav_id = int(request.POST.get('fav_id', 0))
            fav_type = int(request.POST.get('fav_type', ''))

            # 是否已经收藏
            existed_records = UserFavorite.objects.filter(
                user=request.user, fav_id=fav_id, fav_type=fav_type)
            if existed_records:
                existed_records.delete()
                if fav_type == 1:
                    course = Course.objects.get(id=fav_id)
                    course.fav_nums -= 1
                    course.save()
                elif fav_type == 2:
                    course_org = CourseOrg.objects.get(id=fav_id)
                    course_org.fav_nums -= 1
                    course_org.save()
                elif fav_type == 3:
                    teacher = Teacher.objects.get(id=fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()
                return JsonResponse({
                    'status': 'success',
                    'msg': '收藏'
                })
            else:
                user_fav = UserFavorite()
                user_fav.fav_id = fav_id
                user_fav.user = request.user
                user_fav.fav_type = fav_type
                user_fav.save()
                if fav_type == 1:
                    course = Course.objects.get(id=fav_id)
                    course.fav_nums += 1
                    course.save()
                elif fav_type == 2:
                    course_org = CourseOrg.objects.get(id=fav_id)
                    course_org.fav_nums += 1
                    course_org.save()
                elif fav_type == 3:
                    teacher = Teacher.objects.get(id=fav_id)
                    teacher.fav_nums += 1
                    teacher.save()
                return JsonResponse({
                    'status': 'success',
                    'msg': '已收藏'
                })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '参数错误！'
            })
