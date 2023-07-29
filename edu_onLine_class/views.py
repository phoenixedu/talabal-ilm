from django.shortcuts import render, redirect,get_object_or_404
from edu.models import xEduInstitution
from django.views.generic import View,ListView,DetailView
from .forms import ClassOfStudentsForm,EletureForm,electureNotesForm
from .models import ClassOfStudents,Electure,Attendance,electureNotes
from edu_members.models import eduStudents
from datetime import datetime,date,timedelta
from django.utils import timezone

class ClassOfStudentsViewForm(View):
    model = ClassOfStudents
    form_class = ClassOfStudentsForm
    template_name = 'onLine_class/classForm.html'

    def get(self, request, pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        if request.user:
            form = self.form_class(edu=edu)
            return render(request, self.template_name, {'edu': edu, 'form': form})
        else:
            return redirect('classCList', pk_key)
    
    def post(self, request, pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        if request.user:
            form = self.form_class(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('classCList', pk_key)
            return render(request, self.template_name, {'edu': edu, 'form': form})
        else:
            return redirect('classCList', pk_key)
        
class ClassOfStudentsListView(ListView):
    model = ClassOfStudents
    template_name = 'onLine_class/listOfClasses.html'
    context_object_name = 'class_of_students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edu = get_object_or_404(xEduInstitution, pk_key=self.kwargs['pk_key'])
        context['edu'] = edu
        return context
    
class ClassOfStudentsDetailView(DetailView):
    model = ClassOfStudents
    template_name = 'onLine_class/classD.html'
    context_object_name = 'class_of_students'
    def get(self, request, pk_key,pk,name):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        cls = get_object_or_404(ClassOfStudents, pk=pk,name=name)

        today = date.today()
        day = today.strftime("%A")
        leactures = Electure.objects.filter(Eclass=cls,date__date=datetime.today())
        lent = leactures.count()
        now = timezone.now() + timedelta(hours=1)
        now_time = now.time()
        for leacture in leactures:
            lecture_time = leacture.date.time()
            leacture.over = lecture_time <= now_time
            leacture.save()
        return render(request, self.template_name,
                       {
                           'lent':lent,
                            'leactures':leactures,
                            'edu': edu,
                            'today':today,
                            'day':day,
                            'class_of_students': cls,
                        }
                    )
    
    def post(self,request,pk_key,pk,name):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        cls = get_object_or_404(ClassOfStudents,pk=pk,name=name)
        student_id = request.POST.get('student_id')  
        action = request.POST.get('action')
        if action == 'remove':
            student = eduStudents.objects.get(id=student_id)
            student.equiet = False
            student.save()
            cls.studentsOfclass.remove(student)
        return redirect(request.path)
    
class addStudentList(ListView):
    model = eduStudents
    template_name = "onLine_class/addstudentList.html"
    context_object_name = "addListOfStudent"
    def post(self,request,*args, **kwargs):
        edu_pk_key = self.kwargs.get('pk_key')
        pk = self.kwargs.get('pk')
        name = self.kwargs.get('name')
        edu = get_object_or_404(xEduInstitution, pk_key=edu_pk_key)
        cls = get_object_or_404(ClassOfStudents,pk=pk,name=name)
        student_id = request.POST.get('student_id') 
        action = request.POST.get('action')  
        if action == 'add':
            student = eduStudents.objects.get(id=student_id)
            student.equiet = True
            student.save()
            cls.studentsOfclass.add(student)
        return redirect(request.path)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_key=self.kwargs['pk_key']
        pk=self.kwargs['pk']
        name = self.kwargs['name']
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key )
        cls = get_object_or_404(ClassOfStudents,pk=pk,name=name)
        context['edu'] = edu
        context['cls'] = cls
        return context

class createElecture(View):
    model = Electure
    form_class = EletureForm
    template_name = "onLine_class/createLeture.html"

    def get(self, request, pk_key,pk,name):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        cls = get_object_or_404(ClassOfStudents, pk=pk,name=name)
        if request.user:
            form = self.form_class()
            return render(request, self.template_name, {'edu': edu, 'cls':cls ,'form': form})
        else:
            return redirect('classCD', pk_key,pk,name)
    def post(self, request, pk_key,pk,name):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        cls = get_object_or_404(ClassOfStudents, pk=pk,name=name)
        if request.user:
            form = self.form_class(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                # Get the date and time values from the QueryDict
                date = request.POST.get('date_0', '')
                time = request.POST.get('date_1', '')
                datetime_str = f"{date} {time}"
                custom_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
                custom_datetime = timezone.make_aware(custom_datetime)

                instance.date = custom_datetime
                instance.Eclass = cls
                instance.save()

                return redirect('classCD', pk_key,pk,name)
            return render(request, self.template_name, {'edu': edu,'cls':cls, 'form': form})
        else:
            return redirect('classCD', pk_key,pk,name)

class eLactureDatile(DetailView):
    model = Electure
    template_name = "onLine_class/lectureD.html"
    context_object_name = "leacture"

    def get(self,request,pk_key,cls_key,pk,name):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        cls = get_object_or_404(ClassOfStudents,cls_key=cls_key)
        lecture = get_object_or_404(Electure,pk=pk,title=name)
        absent_students = ClassOfStudents.objects.filter(student_att__lecture=lecture, student_att__is_present=False, student_att__on_leave=False).count()
        present_students = ClassOfStudents.objects.filter(student_att__lecture=lecture, student_att__is_present=True).count()
        leave_students = ClassOfStudents.objects.filter(student_att__lecture=lecture, student_att__on_leave=True).count()
        notes = electureNotes.objects.filter(lecture=lecture)
        form = electureNotesForm()
        contx = {
            'notes':notes,
            'absent_students':absent_students,
            'present_students':present_students,
            'leave_students':leave_students,
            'edu':edu,
            'cls':cls,
            'lecture':lecture,
            'form':form,
        }
        return render(request,self.template_name,contx)
    def post(self,request,pk_key,cls_key,pk,name):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        cls = get_object_or_404(ClassOfStudents,cls_key=cls_key)
        lecture = get_object_or_404(Electure,pk=pk,title=name)
        form = electureNotesForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lecture = lecture
            instance.save()
            return redirect(request.path)

class eLactureAttendence(View):
    template_name = "onLine_class/attSheet.html"
    def get(self,request,*args, **kwargs):
        pk_key = kwargs.get('pk_key')
        pk = kwargs.get('pk')
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        lecture = get_object_or_404(Electure,pk=pk)
        cls = lecture.Eclass
        all_students =  cls.studentsOfclass.all()
        absent_students = ClassOfStudents.objects.filter(student_att__lecture=lecture, student_att__is_present=False, student_att__on_leave=False)
        present_students = ClassOfStudents.objects.filter(student_att__lecture=lecture, student_att__is_present=True)
        leave_students = ClassOfStudents.objects.filter(student_att__lecture=lecture, student_att__on_leave=True)
        
        contx = {
            'absent_students':absent_students,
            'present_students':present_students,
            'leave_students':leave_students,
            'edu':edu,
            'cls':cls,
            'lecture':lecture,
        }
        return render(request,self.template_name,contx)
    def post(self,request,*args, **kwargs):
        pk_key = kwargs.get('pk_key')
        pk = kwargs.get('pk')
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        lecture = get_object_or_404(Electure,pk=pk)
        lecture_id = lecture.id
        cls = lecture.Eclass
        student_id = request.POST.get('student_id') 
        action = request.POST.get('action')  
        student_attendance, created = Attendance.objects.get_or_create(
            student_id=student_id,
            lecture_id=lecture_id
        )

        if action == 'present':
            student_attendance.is_present = True
            student_attendance.on_leave = False
            student_attendance.attendance_time = datetime.now()
        elif action == 'absent':
            student_attendance.is_present = False
            student_attendance.on_leave = False
            student_attendance.attendance_time = datetime.now()
        elif action == 'leave':
            student_attendance.is_present = False
            student_attendance.on_leave = True
            student_attendance.attendance_time = datetime.now()

        student_attendance.save()

        
        return redirect(request.path)

class listOfElectures(ListView):
    model = Electure
    template_name = "onLine_class/listofLecture.html"
    context_object_name = "all_lecture"

    def get(self,request,pk_key,cls_key):
        edu = get_object_or_404(xEduInstitution , pk_key=pk_key)
        cls = get_object_or_404(ClassOfStudents,cls_key=cls_key)
        all_lecture = Electure.objects.filter(Eclass=cls)
        contx = {
            'edu':edu,
            'cls':cls,
            self.context_object_name:all_lecture,
        }
        return render(request,self.template_name,contx)
    def post(self,request,pk_key,cls_key):
        edu = get_object_or_404(xEduInstitution , pk_key=pk_key)
        cls = get_object_or_404(ClassOfStudents,cls_key=cls_key)
        all_lecture = Electure.objects.filter(Eclass=cls)
        lecture_id = request.POST.get('lecture_id')
        action = request.POST.get('action')
        lecture = Electure.objects.get(id=lecture_id)
        if action == "cancel":
            lecture.cancel = True
            lecture.save()
        elif action == "undo":
            lecture.cancel = False
            lecture.save()
        return redirect(request.path)
    