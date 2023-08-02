from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,ListView,DetailView
from edu.models import xEduInstitution,userEdu
from django.http import FileResponse,HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .models import jobCvForm,studentAdmitForm,eduStudents,eduFaculty
from .forms import JobAppliCvForm,StudenAddmissionPanddingForm
from edu_recruiter.models import AdmissionFrom,jobRecruitry
from blogs_post.models import DefaltBlogPost
from edu_permissions.models import GroupOfStudents
from django.contrib.auth.mixins import PermissionRequiredMixin
import os


# Create your views here.
class admFormsView(View):
    model = None
    form_class = None
    template_name = None
    adm_Object = None
    
    def get(self,request,pk_key,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        adm = get_object_or_404(self.adm_Object,pk=pk)
        if  request.user.has_perm('edu_members.can_create_edu_models'):
            form = self.form_class()
            return render(request,self.template_name,{'edu':edu,'adm':adm,'form':form})
        else:
            return redirect('eduD', pk_key)
    def post(self,request,pk_key,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        adm = get_object_or_404(self.adm_Object,pk=pk)
        if  request.user.has_perm('edu_members.can_create_edu_models'):
            form = self.form_class(request.POST,request.FILES)
            if form.is_valid() :
                instance = form.save(commit=False)
                instance.userS = request.user
                instance.admForm = adm
                instance.save()
                return redirect('eduD', pk_key)
            return render(request,self.template_name,{'edu':edu,'adm':adm,'form':form})
        else:
            return redirect('eduD', pk_key)

def view_file(request, file_url):
    file_path = os.path.join(settings.MEDIA_ROOT, file_url[len(settings.MEDIA_URL):].replace('/', os.path.sep))
     
    if os.path.exists(file_path):
        try: 
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension == '.pdf':
                content_type = 'application/pdf'
            elif file_extension == '.docx':
                content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            else:
                return HttpResponse("Unsupported file format")

            # with open(file_path, 'rb') as f:
            try:
                f = open(file_path, 'rb')
                response = FileResponse(f, content_type=content_type)
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
            except Exception as e:
                return HttpResponse(str(e))
            finally:
                f.close()
        except FileNotFoundError:
            return HttpResponse("File not found first")
    else:
        return HttpResponse("File path does not exist")

class CreateStudentAdmission(admFormsView):
    model = studentAdmitForm
    form_class = StudenAddmissionPanddingForm
    adm_Object = AdmissionFrom
    template_name = 'members/studentAdmissionForm.html'

class CreateEmpolyJoinning(admFormsView):
    model = jobCvForm
    form_class = JobAppliCvForm
    adm_Object = jobRecruitry
    template_name = 'members/empolyeesCvForm.html'

class viewStudentApplication(PermissionRequiredMixin,ListView):
    model = studentAdmitForm
    context_object_name = "applications"
    template_name = 'members/studentList.html'
    permission_required = "edu_members.can_view_groups_edu"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edu = get_object_or_404(xEduInstitution, pk_key=self.kwargs['pk_key'])
        context['edu'] = edu
        return context
    
    def handle_no_permission(self):
        return redirect('home') 
    
    def post(self, request,pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        if  request.user.has_perm('edu_members.can_approve_student_request_edu'):
            student_id = request.POST.get('student_id')
            status = request.POST.get('status')
            student = studentAdmitForm.objects.get(id=student_id)
            student.status = status
            student.save()
            if status == 'Approved':
                instance = eduStudents(edu=edu, dataForm=student,user=student.userS)
                instance.save()
                try:
                    userEdu.objects.get_or_create(edu=edu,user=student.userS,study_at=True)
                    edugrp_std,_ = GroupOfStudents.objects.get_or_create(edu=edu)
                    edugrp_std.members.add(instance)
                    edugrp_std.save()
                    
                except:
                    pass
                return redirect('LOA',  pk_key)
        else:
            return redirect('LOA',  pk_key)

class viewEmpolyCv(PermissionRequiredMixin,ListView):
    model = jobCvForm
    context_object_name = "applications"
    template_name = 'members/empolyList.html'
    permission_required = "edu_members.can_edit_edu_lvl3"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edu = get_object_or_404(xEduInstitution, pk_key=self.kwargs['pk_key'])
        context['edu'] = edu
        return context
    
    def handle_no_permission(self):
        return redirect('home') 
    
    def post(self, request,pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        if  request.user.has_perm('edu_members.can_approve_job_request_edu'):
            employees_id = request.POST.get('employees_id')
            status = request.POST.get('status')
            employees = jobCvForm.objects.get(id=employees_id)
            employees.status = status
            employees.save()
            if status == 'Approved':
                instance = eduFaculty(edu=edu, dataForm=employees, user=employees.userS)
                instance.save()
                try:
                    DefaltBlogPost.objects.create(
                        key = instance.eduID,
                        title = instance.user,
                        content= f'About {instance.user}',
                    )
                    try:
                        userEdu.objects.get_or_create(edu=edu,user=employees.userS,work_at=True)
                    except:
                        pass
                except:
                    pass
                return redirect('CVs',  pk_key)
        else:
            return redirect('CVs',  pk_key)

class ListOfEduFaculties(ListView):
    model = eduFaculty
    template_name = "members/facultyList.html"
    context_object_name = 'allFaculties'
    def get(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        listOfFaculties = eduFaculty.objects.filter(edu=edu)
        numOfFaculties = listOfFaculties.count()
        if request.user.has_perm('edu_members.can_view_groups_edu'):
            contx = {
                'edu':edu,
                self.context_object_name:listOfFaculties,
                'countFlty':numOfFaculties,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('eduD',pk_key=pk_key)

class ListOfEduStudents(ListView):
    model = eduStudents
    template_name = "members/studentslist.html"
    context_object_name = 'allstudents'
    def get(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        listOfStudents = eduStudents.objects.filter(edu=edu)
        numOfStudents = listOfStudents.count()
        if  request.user.has_perm('edu_members.can_can_view_edu_models'):
            contx = {
                'edu':edu,
                self.context_object_name:listOfStudents,
                'countstudent':numOfStudents,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('eduD',pk_key=pk_key)
    
class DataileOfEduFaculty(DetailView):
    model = eduFaculty
    template_name = "members/facultyEduProfile.html"
    context_object_name = 'faculty'
    def get(self,request,pk_key,eduID):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        faculty = get_object_or_404(eduFaculty,eduID=eduID)
        blog, _ = DefaltBlogPost.objects.get_or_create(key=faculty.eduID)
        contx={
            'blog':blog,
            'edu':edu,
            self.context_object_name:faculty,
        }
        return render(request,self.template_name,contx)
    
class DatileOfEduStudent(DetailView):
    model = eduStudents
    template_name = "members/studentEduProfile.html"
    context_object_name = 'student'
    def get(self,request,pk_key,eduID):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        student = get_object_or_404(eduStudents,eduID=eduID)
        if  request.user.has_perm('edu_members.can_can_view_edu_models'):
            blog, _ = DefaltBlogPost.objects.get_or_create(key=student.eduID)
            contx={
                'blog':blog,
                'edu':edu,
                self.context_object_name:student,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('eduD',pk_key=pk_key)