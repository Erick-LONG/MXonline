from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg,City
# Create your views here.


class OrgView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        org_nums = all_orgs.count()
        return render(request,'org-list.html',{
            "all_orgs":all_orgs,
            "all_citys":all_citys,
            'org_nums':org_nums
        })