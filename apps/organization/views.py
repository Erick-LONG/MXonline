from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import CourseOrg,City,Teacher
from pure_pagination import PageNotAnInteger,Paginator
from .forms import UserAskForm
from operation.models import UserFavorite
from courses.models import Course
# Create your views here.


class OrgView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        all_citys = City.objects.all()

        #取出筛选城市
        city_id = request.GET.get('city','')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 筛选类别
        category = request.GET.get('ct','')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort=='students':
                all_orgs = all_orgs.order_by('-student')
            elif sort =='courses':
                all_orgs = all_orgs.order_by('-course_num')


        org_nums = all_orgs.count()

        #对课程机构进行分页
        try:
            page_num = request.GET.get('page',1)
        except PageNotAnInteger:
            page_num = 1

        p =Paginator(all_orgs,5,request=request)
        orgs=p.page(page_num)
        return render(request,'org-list.html',{
            "all_orgs":orgs,
            "all_citys":all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })


class AddUserAskView(View):
    def post(self,request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            user_ask =user_ask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}',content_type='application/json')


class OrgHomeView(View):
    def get(self,request,org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id = int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,fav_id=course_org.id,fav_type=2):
                has_fav =True
        all_course = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:3]
        return render(request,'org-detail-homepage.html',{
            'all_course':all_course,
            'all_teacher':all_teachers,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav':has_fav,
        })


class OrgCourseView(View):
    def get(self,request,org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id = int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_course = course_org.course_set.all()
        return render(request,'org-detail-course.html',{
            'all_course':all_course,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav': has_fav,
        })


class OrgDescView(View):
    def get(self,request,org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id = int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-desc.html',{
            'course_org':course_org,
            'current_page':current_page,
            'has_fav': has_fav,
        })


class OrgTeacherView(View):
    def get(self,request,org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id = int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_teacher = course_org.teacher_set.all()
        return render(request,'org-detail-teachers.html',{
            'all_teacher':all_teacher,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav': has_fav,
        })


class AddFavView(View):
    def post(self,request):
        fav_id = request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type',0)

        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')

        exist_record = UserFavorite.objects.filter(user=request.user,fav_id=int(fav_id),fav_type=int(fav_type))
        if exist_record:
            #如果记录已经存在，就取消收藏
            exist_record.delete()
            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id)>0 and int(fav_type)>0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')


class TeacherListView(View):
    def get(self,request):
        all_teachers = Teacher.objects.all()
        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                all_teachers = all_teachers.order_by('-click_nums')

        #讲师排行榜
        sorted_teacher = Teacher.objects.all().order_by('-click_nums')[:3]

        # 对讲师进行分页
        try:
            page_num = request.GET.get('page', 1)
        except PageNotAnInteger:
            page_num = 1

        p = Paginator(all_teachers, 2, request=request)
        teachers = p.page(page_num)
        return render(request,'teachers-list.html',{
            'all_teachers':teachers,
            'sorted_teacher':sorted_teacher,
            'sort':sort,
        })


class TeacherDetailView(View):
    def get(self,request,teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        all_courses = Course.objects.filter(teacher=teacher)

        has_teacher_faved = False
        if UserFavorite.objects.filter(user = request.user,fav_type=3,fav_id=teacher.id):
            has_teacher_faved = True

        has_org_fabed = False
        if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=teacher.org.id):
            has_org_fabed = True

        # 讲师排行榜
        sorted_teacher = Teacher.objects.all().order_by('-click_nums')[:3]
        return render(request,'teacher-detail.html',{
            'teacher':teacher,
            'all_courses':all_courses,
            'sorted_teacher':sorted_teacher,
            'has_teacher_faved':has_teacher_faved,
            'has_org_fabed':has_org_fabed,
        })