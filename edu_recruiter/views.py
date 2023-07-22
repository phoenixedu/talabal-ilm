from django.shortcuts import render,get_object_or_404,redirect
from .models import AdmissionFrom, jobRecruitry
from .forms import AdmissionFromForm, jobRecruitryForm
from edu_stracture.eduCustomViews import eduAsPk
from django.views.generic import DetailView,View
from edu_stracture.models import eduRole
from edu.models import InstCourse,xEduInstitution

class CreateAdmission(View):
    model = AdmissionFrom
    form_class = AdmissionFromForm
    template_name = "recruiter/admissionposter.html"
    
    def get(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        course = InstCourse.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = self.form_class()
            return render(request,self.template_name,{'form':form,'edu':edu,'course_all':course})
        else :
            return redirect('eduAdmin',pk_key)
    def post(self, request, pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        courseID = InstCourse.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = self.form_class(request.POST,request.FILES,edu=edu)
            if form.is_valid():
                semester = form.save(commit=False)
                semester.edu = edu
                semester.save()
                form.save_m2m()
                selected_course_ids = request.POST.getlist('selected_courses')
                selected_courses = courseID.filter(pk__in=selected_course_ids)
                semester.course.set(selected_courses)     
                return redirect('eduAdmin',pk_key)
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return redirect('eduAdmin',pk_key)
        
class CreateJobRecruitry(View):
    model = jobRecruitry
    form_class = jobRecruitryForm
    template_name = 'recruiter/jobposter.html'
    
    def get(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        course = eduRole.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = self.form_class()
            return render(request,self.template_name,{'form':form,'edu':edu,'course_all':course})
        else :
            return redirect('eduAdmin',pk_key)
    def post(self, request, pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        jobID = eduRole.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = self.form_class(request.POST,request.FILES,edu=edu)
            if form.is_valid():
                post_j = form.save(commit=False)
                post_j.edu = edu
                post_j.save()
                form.save_m2m()
                selected_job_ids = request.POST.getlist('selected_jobs')
                selected_jobs = jobID.filter(pk__in=selected_job_ids)
                post_j.forPost.set(selected_jobs)     
                return redirect('eduAdmin',pk_key)
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return redirect('eduAdmin',pk_key)

class JobRecruitryDetailView(DetailView):
    model = jobRecruitry
    template_name = 'recruiter/jobD.html'
    context_object_name = 'job'

    def get(self,request,pk_key,pk,name):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        onj = get_object_or_404(self.model,pk=pk,name=name)
        return render(request,self.template_name,{self.context_object_name:onj,'edu':edu})

class admissionDV(DetailView):
    model = AdmissionFrom
    template_name = 'recruiter/AdmissionD.html'
    context_object_name = 'admis'

    def get(self,request,pk_key,pk,name):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        onj = get_object_or_404(self.model,pk=pk,name=name)
        return render(request,self.template_name,{self.context_object_name:onj,'edu':edu})
