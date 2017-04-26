from django.shortcuts import render
from myprofile.models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'myprofile/index.html', {'message' : 'First test done'})

def profile(request):
    profile = profileinfo.objects.get(name='Nurendra Choudhary')
    achievement = achievements.objects.filter(id__gte = 0).order_by('-importance')
    activities = cocurricular.objects.filter(id__gte = 0).order_by('-importance')
    educations = education.objects.filter(id__gte = 0).order_by('-id')
    experiences = work_experience.objects.filter(id__gte = 0).order_by('-importance')
    return render(request, 'myprofile/profile.html',{'profile' : profile,'achievements':achievement,'activities':activities,'educations':educations,'experiences':experiences})

def research(request):
    publication_rows = publications.objects.filter(id__gte = 0).order_by('-importance')
    profile_rows = profiles.objects.filter(Q(types='Research') | Q(types='Misc')).order_by('-importance')
    project_rows = projects.objects.filter(Q(types='Research') | Q(types='Misc')).order_by('-importance')
    return render(request, 'myprofile/research.html',{'publications': publication_rows,'profiles':profile_rows,'projects':project_rows})

def developer(request):
    main_profile = profileinfo.objects.get(name='Nurendra Choudhary')
    profile_rows = profiles.objects.filter(Q(types='Research') | Q(types='Misc')).order_by('-importance')
    project_rows = projects.objects.filter(Q(types='Research') | Q(types='Misc')).order_by('-importance')
    return render(request,'myprofile/developer.html',{'profiles':profile_rows,'projects':project_rows,'main_profile':main_profile})
