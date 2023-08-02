from .forms import eduDepartmentForm,eduClassForm,eduLabForm,eduRoleForm,eduSocietyForm
from .models import eduDepartment,eduClass,eduLab,eduRole,eduSociety
from .eduCustomViews import EduFormsView,EduFilterFormsView
from django.views.generic import View,DetailView
from django.shortcuts import render ,get_object_or_404,redirect
from edu.models import xEduInstitution
from edu_recruiter.models import jobRecruitry,AdmissionFrom
from edu_members.models import eduFaculty,eduStudents
from blogs_post.models import DefaltBlogPost
from edu_permissions.models import HeadOfTheDepartment,InchargeOfClass
from edu_onLine_class.models import ClassOfStudents

# Create your views here.
class eduAdmin(View):
    template_name = "eduAdmin.html"
    def get(self, request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        if request.user.has_perm('edu_members.can_view_edu_admin_page'):
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
        else:
            return redirect('eduD' , pk_key=pk_key)
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

class eduDeptView(DetailView):
    model = eduDepartment
    context_object_name = "dept"
    template_name = "stracture/departmentD.html"

    def get(self,request,pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        dept = get_object_or_404(eduDepartment,name=name,pk=pk)
        class_list = eduClass.objects.filter(edu=edu)
        key = f"{pk_key}_department_09.{pk}"
        Defaltpost,_ = DefaltBlogPost.objects.get_or_create(key=key)
        hodName= f"Head Of {dept.name}"
        hod,_ = HeadOfTheDepartment.objects.get_or_create(edu=edu,department=dept,name=hodName)
        head = None
        for r in hod.members.all():
            if r:
                head = r
        contx = {
            'class_list':class_list,
            'hod':hod,
            'head':head,
            'edu':edu,
            'Defaltpost':Defaltpost,
            self.context_object_name : dept,
        }
        return render(request,self.template_name,contx)

class eduClassDeView(DetailView):
    model = eduClass
    context_object_name = "cls"
    template_name = "stracture/deptClassD.html"

    def get(self,request,pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        Eclass = get_object_or_404(eduClass,name=name,pk=pk)
        classd = ClassOfStudents.objects.filter(Eclass=Eclass)
        if request.user.has_perm('edu_members.can_can_view_edu_models'):
            contx = {
                'edu':edu,
                'get_class':classd,
                self.context_object_name : Eclass,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect("eduAdmin",pk_key=pk_key)