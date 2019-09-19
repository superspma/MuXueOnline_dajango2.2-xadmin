from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='课程名', max_length=50)
    desc = models.CharField(verbose_name='课程描述', max_length=300)
    learn_time = models.IntegerField(verbose_name='学习时长（分钟数）', default=0)
    degree = models.CharField(verbose_name='难度', choices=(
        ('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2)
    students = models.IntegerField(verbose_name='学习人数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数', default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    category = models.CharField(verbose_name='课程类别', default=u'后端开发', max_length=20)
    tag = models.CharField(verbose_name='课程标签', default='', max_length=10)
    youneed_know = models.CharField(verbose_name='课程须知', default='', max_length=300)
    teacher_tell = models.CharField(verbose_name='老师告诉你', default='', max_length=300)

    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(verbose_name='封面图', upload_to='courses/%Y%m', max_length=100)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'章节名', max_length=100)
    learn_times = models.IntegerField(verbose_name=u'学习时长（分钟数）', default=0)

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'视频名', max_length=100)
    learn_times = models.IntegerField(verbose_name=u'学习时长（分钟数）', default=0)
    url = models.CharField(verbose_name=u'访问地址', max_length=200)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'名称', max_length=100)
    file = models.FileField(verbose_name='下载地址', upload_to='course/resource/%Y%m', max_length=200)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
