from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import Course
from pure_pagination import PageNotAnInteger,Paginator


class CourseView(View):
    def get(self,request):
        all_courses = Course.objects.all().order_by('-add_time')
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]
        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by('-students')
            elif sort == 'hot':
                all_courses = all_courses.order_by('-click_nums')

        # 对课程进行分页
        try:
            page_num = request.GET.get('page', 1)
        except PageNotAnInteger:
            page_num = 1

        p = Paginator(all_courses, 6, request=request)
        courses = p.page(page_num)
        return render(request,'course-list.html',{'all_courses':courses,
                                                  'sort':sort,
                                                  'hot_courses':hot_courses})


class CourseDetailView(View):
    def get(self,request,course_id):
        course = Course.objects.get(id = int(course_id))
        course.click_nums +=1
        course.save()
        return render(request,'course-detail.html',{'course':course})