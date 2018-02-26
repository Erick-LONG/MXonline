from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg,City
from pure_pagination import PageNotAnInteger,Paginator
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