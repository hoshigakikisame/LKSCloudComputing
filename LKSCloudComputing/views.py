from django.shortcuts import render
import extracurricular
from schoolprofile import models
from achievement import models as achievementmodels
from major import models as majormodels
from schoolactivity import models as activitymodels
from extracurricular import models as extracurricularmodels
from teacher import models as teachermodels


def index(request):

    schoolProfile = models.SchoolProfile.objects.all()[0]
    achievements = achievementmodels.Achievement.objects.all()
    majors = majormodels.Major.objects.all()
    activities = activitymodels.SchoolActivity.objects.all()
    extracurriculars = extracurricularmodels.Extracurricular.objects.all()
    teachers = teachermodels.Teacher.objects.all()

    context = {
        'schoolProfile' : schoolProfile,
        'achievements': achievements,
        'majors': majors,
        'activities': activities,
        'extracurriculars': extracurriculars,
        'teachers': teachers
    }

    return render(request, 'index.html', context)