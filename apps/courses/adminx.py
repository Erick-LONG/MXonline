from .models import Course,Lesson,Video,CourseResource
import xadmin


class CourseAdmin():
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']


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
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)