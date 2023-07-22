from .forms import eduDepartmentForm,eduClassForm,eduLabForm,eduRoleForm,eduSocietyForm
from .models import eduDepartment,eduClass,eduLab,eduRole,eduSociety
from .eduCustomViews import EduFormsView,EduFilterFormsView
from django.views.generic import View
from django.shortcuts import render ,get_object_or_404
from edu.models import xEduInstitution
from edu_recruiter.models import jobRecruitry,AdmissionFrom
from edu_members.models import eduFaculty,eduStudents
# Create your views here.
class eduAdmin(View):
    template_name = "eduAdmin.html"
    def get(self, request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        class_list = eduClass.objects.filter(edu=edu)
        dept_list = eduDepartment.objects.filter(edu=edu)
        labs_list = eduLab.objects.filter(edu=edu)
        cv_poster = jobRecruitry.objects.filter(edu=edu)
        admision_poster = AdmissionFrom.objects.filter(edu=edu)
        faculty_list = eduFaculty.objects.filter(edu=edu)
        contFlty = faculty_list.count()
        student_list = eduStudents.objects.filter(edu=edu)
        contStudent = student_list.count()
        contx = {
            'faculty_list':faculty_list,
            'contFlty':contFlty,
            'student_list':student_list,
            'contStudent':contStudent,
            'class_list':class_list,
            'dept_list':dept_list,
            'labs_list':labs_list,
            'cv_poster':cv_poster,
            'admision_poster':admision_poster,
            'edu':edu,
        }
        return render(request,self.template_name,contx)
class creatDept(EduFormsView):
    model = eduDepartment
    form_class = eduDepartmentForm
    template_name = 'stracture/add_department.html'

class creatClass(EduFilterFormsView):
    model = eduClass
    form_class = eduClassForm
    template_name = 'stracture/add_class.html'

class creatLab(EduFilterFormsView):
    model = eduLab
    form_class = eduLabForm
    template_name = "stracture/add_lab.html"

class creatRole(EduFormsView):
    model = eduRole
    form_class = eduRoleForm
    template_name = "stracture/add_roles.html"
class createSociety(EduFormsView):
    model = eduSociety
    form_class = eduSocietyForm
    template_name = "stracture/add_society.html"

