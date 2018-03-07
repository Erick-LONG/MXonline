from .models import Course,Lesson,Video,CourseResource,BannerCourse
import xadmin
from organization.models import CourseOrg

class LessonInLine():
    model = Lesson
    extra = 0


class CourseResourceInLine():
    model = CourseResource
    extra = 0


class CourseAdmin():
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time','get_zj_nums','go_to']
    search_fields = ['name', 'desc', 'detail', 'degree','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    ordering = ['-click_nums']#排序
    readonly_fields = ['click_nums']#只读
    list_editable = ['degree','desc']#可直接修改编辑字段
    exclude = ['fav_nums']#隐藏
    inlines = [LessonInLine,CourseResourceInLine] #直接添加章节和课程资源信息
    #refresh_times = [3,5] 每隔多长时间刷新一次
    style_fields = {'detail':'ueditor'}

    def queryset(self): #筛选表分别管理
        qs = super(CourseAdmin,self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        #在保存课程的时候统计课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


class BannerCourseAdmin():
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    ordering = ['-click_nums']#排序
    readonly_fields = ['click_nums']#只读
    exclude = ['fav_nums']#隐藏
    inlines = [LessonInLine,CourseResourceInLine] #直接添加章节和课程资源信息

    def queryset(self):
        qs = super(BannerCourseAdmin,self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin():
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin():
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name', ]
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin():
    list_display = ['course', 'name','down_load','add_time']
    search_fields = ['course', 'name']
    list_filter = ['course','name','down_load','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)