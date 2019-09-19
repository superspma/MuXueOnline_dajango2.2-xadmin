from django.db import models

# Create your models here.
from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(verbose_name=u'城市', max_length=20)
    desc = models.CharField(verbose_name=u'描述', max_length=200)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class CourseOrg(BaseModel):
    name = models.CharField(verbose_name='机构名称', max_length=50)
    desc = models.TextField(verbose_name='描述')
    tag = models.CharField(verbose_name='机构标签', default='全国知名', max_length=10)
    calegory = models.CharField(verbose_name='机构类别', default='pxjg', max_length=4,
                                choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')))
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    image = models.ImageField(verbose_name=u'logo', max_length=100, upload_to='org/%Y/%m')
    address = models.CharField(verbose_name='机构地址', max_length=150)
    students = models.IntegerField(verbose_name='学习人数', default=0)
    course_nums = models.IntegerField(verbose_name='课程数', default=0)
    city = models.ForeignKey(City, verbose_name='所在城市', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'教师名', max_length=50)
    work_years = models.IntegerField(verbose_name='工作年限', default=0)
    work_company = models.CharField(verbose_name='就职公司', max_length=50)
    work_position = models.CharField(verbose_name='公司职位', max_length=50)
    points = models.CharField(verbose_name='教学特点', max_length=50)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    age = models.IntegerField(verbose_name='年龄', default=18)
    image = models.ImageField(verbose_name='头像', upload_to='teacher/%Y/%m', max_length=100)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
