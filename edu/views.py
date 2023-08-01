from django.shortcuts import render ,redirect
from django.views.generic import DetailView,UpdateView
from django.views import View
from .models import xEduInstitution,InstCourse,Semester,Book,userEdu
from django.shortcuts import get_object_or_404
from .forms import  InstCourseForm, SemesterForm,updateSemester,BookForm,updateCourse,xEduInstitutionForm,updateEDU
from django.urls import reverse_lazy
from blogs_post.models import DefaltBlogPost
from edu_permissions.models import HeadOfInstetude
from edu_members.models import eduFaculty 

# view functions
class createInstetude(View):
    template_name = 'edu/eduForm.html'
    form_class = xEduInstitutionForm
    def get(self,request):
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request,self.template_name,{'form':form})
        else:
            return redirect('home')
    def post(self, request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.OwnerOfX = request.user
            instance.save()
            user = instance.OwnerOfX
            try:
                DefaltBlogPost.objects.create(
                    key = instance.pk_key,
                    title = instance.name,
                    content = f'Description for {instance.name}',
                )
                user = instance.OwnerOfX
                try:
                    faculty,_ = eduFaculty.objects.get_or_create(edu=instance,user=user,equiet=True)
                    head,_= HeadOfInstetude.objects.get_or_create(edu=instance)
                    head.members.add(faculty)
                    head.save()
                except:
                    pass
                try:
                    get,create =userEdu.objects.get_or_create(user=user,edu=instance,work_at=True)
                except:
                    pass
                
            except:
                pass
            return redirect('home')
        return render(request, self.template_name, {'form': form})
    
class create_InstCourse(View): 
    template_name = 'edu/courseForm.html'
    def get(self, request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        course_list = InstCourse.objects.filter(edu=edu)
        if  request.user == edu.OwnerOfX:
            form = InstCourseForm()
            return render(request, self.template_name ,{'edu':edu ,'course_list':course_list,'form':form})
        else:
            return redirect('eduD',pk_key)
    def post(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        if request.user == edu.OwnerOfX:
            form = InstCourseForm(data=request.POST)
            if form.is_valid:
                course = form.save(commit=False)
                course.edu = edu
                course.save()
                return redirect('eduD',pk_key)
        return render(request, self.template_name ,{'edu':edu ,'form':form})
    
class create_semister(View):
    template_name = 'edu/semisterForm.html'
    def get(self,request,pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        course = get_object_or_404(InstCourse,name=name,edu=edu,pk=pk)
        course_list = InstCourse.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = SemesterForm()
            return render(request,self.template_name,{'form':form,'edu':edu,'course':course,'course_list':course_list})
        else :
            return redirect('courseD',pk_key,name,pk)
    def post(self, request, pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        course = get_object_or_404(InstCourse,name=name,edu=edu,pk=pk)
        if request.user == edu.OwnerOfX:
            form = SemesterForm(request.POST)
            if form.is_valid():
                semester = form.save(commit=False)
                semester.course = course
                semester.save()
                form.save_m2m()  # Save the Many-to-Many relationships
                return redirect('courseD',pk_key,name,pk)
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return redirect('courseD',pk,pk_key,name)
        

class xEduInstDetaile(DetailView):
    model = xEduInstitution
    template_name = 'edu/eduD.html'
    context_object_name = 'edu'
    
    def get(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        course_list = InstCourse.objects.filter(edu=edu)
        Defaltpost = DefaltBlogPost.objects.get(key=edu.pk_key)
        return render(request, self.template_name,{
            self.context_object_name:edu,
            'course_list':course_list,
            'Defaltpost':Defaltpost,
        })
    

class courseDetail(DetailView):
    model = InstCourse
    template_name = 'edu/courseD.html'
    context_object_name = 'course'

    def get(self,request,pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        course = get_object_or_404(InstCourse,name=name,pk=pk)
        course_list = InstCourse.objects.filter(edu=edu)
        semisters = Semester.objects.filter(course_id=pk)
        contx = {
            'edu':edu,
            self.context_object_name:course,
            'course_list':course_list,
            'semisters':semisters,
        }
        return render(request,self.template_name,contx)

class createBooks(View):
    model = Book
    template_name = 'edu/bookForm.html'
    form_class = BookForm
    def get(self, request, pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        course = InstCourse.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = self.form_class(edu=edu)
            return render(request, self.template_name, {
                        'form': form,
                        'edu': edu, 
                        'course': course
                    })
        else:
            return redirect('home')
    
    def post(self, request, pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        course = InstCourse.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = self.form_class(request.POST)
            if form.is_valid():
                book = form.save(commit=False)
                book.save()
                course_ids = request.POST.getlist('course')
                book.course.set(course_ids)
                return redirect('eduD',pk_key)
            else:
                return render(request, self.template_name, {
                        'form': form,
                        'edu': edu,
                        'course': course
                    })
        else:
            return redirect('home')
    

class eduInstUpdate(UpdateView):
    model = xEduInstitution
    form_class = updateEDU
    template_name = "edu/eduUpdate.html"
    
    def get_object(self, queryset=None):
        pk_key = self.kwargs.get('pk_key')
        return get_object_or_404(xEduInstitution, pk_key=pk_key)
    def get(self, request, pk_key):
        edu = self.get_object()
        if request.user == edu.OwnerOfX:
            form = self.form_class(instance=edu)
            return render(request, self.template_name, {'edu': edu, 'form': form})
        else:
            return redirect('eduD', pk_key)

    def post(self, request, pk_key):
        edu = self.get_object()
        form = self.form_class(request.POST, request.FILES, instance=edu)
        if form.is_valid():
            form.save()
            try:
                user = edu.OwnerOfX
                faculty,_ = eduFaculty.objects.get_or_create(edu=edu,user=user,equiet=True)
                head,_= HeadOfInstetude.objects.get_or_create(edu=edu)
                head.members.add(faculty)
                head.save()
            except:
                pass
            return redirect('home')
        else:
            return redirect('eduD', pk_key)
    
class InstCourseUdate(UpdateView):
    model = InstCourse
    form_class = updateCourse
    template_name = "edu/couseUpdate.html"
    context_object_name = "course"

    def get(self,request,pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        course = get_object_or_404(InstCourse,name=name,pk=pk)
        course_list = InstCourse.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = self.form_class(instance=course)
            return render(request,self.template_name,{'edu':edu,'course_list':course_list,self.context_object_name:course,'form':form})
        else:
            return redirect('eduD',pk_key)
    def post(self,request,pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        course = get_object_or_404(InstCourse,name=name,pk=pk)
        form = self.form_class(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('eduD',pk_key)
        else:
            return render(request,self.template_name,{'edu':edu,self.context_object_name:course,'form':form})

class semisterUpdate(UpdateView):
    model = Semester
    form_class = updateSemester
    template_name = "edu/semisterUpdate.html"
    context_object_name = "semister"
    def get(self,request,pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        semister = get_object_or_404(Semester,pk=pk)
        course = InstCourse.objects.get(id=semister.course_id,name=name)
        course_list = InstCourse.objects.filter(edu=edu)
        if request.user == edu.OwnerOfX:
            form = self.form_class(instance=semister)
            return render(request,self.template_name,{
                'edu':edu,
                'course_list':course_list,
                self.context_object_name:semister,
                'course':course,
                'form':form})
        else:
            pkC = course.id
            return redirect('courseD',pk_key=pk_key,name=name,pk=pkC)
    def post(self,request,pk_key,name,pk):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        semister = get_object_or_404(Semester,pk=pk)
        course = InstCourse.objects.get(id=semister.course_id,name=name)
        form = self.form_class(request.POST,instance=semister)
        if form.is_valid():
            form.save()
            # form.save_m2m() 
            pkC = course.id
            return redirect('courseD',pk_key=pk_key,name=name,pk=pkC)
        else:
            return render(request,self.template_name,{
                'edu':edu,
                self.context_object_name:semister,
                'course':course,
                'form':form})
        


