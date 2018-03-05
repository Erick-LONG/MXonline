from .models import CourseOrg,City,Teacher
import xadmin


class CityAdmin():
    list_display = ['desc', 'name', 'add_time']
    search_fields = ['desc', 'name']
    list_filter = ['desc', 'name', 'add_time']


class CourseOrgAdmin():
    list_display = ['name', 'desc','add_time','click_nums','fav_nums','image','address','city__name']
    search_fields = ['name', 'desc','click_nums','fav_nums','image','address','city__name']
    list_filter = ['name', 'desc','add_time','click_nums','fav_nums','image','address','city__name']
    relfield_style = 'fk-ajax' #搜索模式，需要把搜索字段中的外键（city）改成(city__name)


class TeacherAdmin():
    list_display = ['org', 'name', 'work_years','work_company','work_position','points','click_nums','fav_nums','add_time']
    search_fields = ['org', 'name', 'work_years','work_company','work_position','points','click_nums','fav_nums']
    list_filter = ['org', 'name', 'work_years','work_company','work_position','points','click_nums','fav_nums','add_time']


xadmin.site.register(City,CityAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)