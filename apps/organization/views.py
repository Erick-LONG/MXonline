from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg,City
from pure_pagination import PageNotAnInteger,Paginator
# Create your views here.


class OrgView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
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

        })