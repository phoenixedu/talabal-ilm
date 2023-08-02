from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.views.generic.list import MultipleObjectMixin
from edu.models import xEduInstitution

class EduFormsView(View):
    model = None
    form_class = None
    template_name = None
    def get(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        if request.user.has_perm('edu_members.can_create_edu_models'):
            form = self.form_class()
            return render(request,self.template_name,{'edu':edu,'form':form})
        else:
            return redirect('eduAdmin',pk_key)
    def post(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        if request.user.has_perm('edu_members.can_create_edu_models'):
            form = self.form_class(request.POST,request.FILES)
            if form.is_valid() :
                instance = form.save(commit=False)
                instance.edu = edu
                instance.save()
                return redirect('eduAdmin', pk_key)
            return render(request,self.template_name,{'edu':edu,'form':form})
        else:
            return redirect('eduAdmin',pk_key)

class EduFilterFormsView(View):
    model = None
    form_class = None
    template_name = None
    m2m_field = None

    def get(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        if request.user.has_perm('edu_members.can_create_edu_models'):
            form = self.form_class(edu=edu)
            return render(request,self.template_name,{'edu':edu,'form':form})
        else:
            return redirect('eduAdmin',pk_key)
    def post(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        if self.m2m_field is not None:
            self.m2m_field = self.m2m_field.objects.filter(edu=edu)
        if request.user.has_perm('edu_members.can_create_edu_models'):
            form = self.form_class(request.POST,request.FILES,edu=edu)
            if form.is_valid() :
                instance = form.save(commit=False)
                instance.edu = edu
                instance.save()
                if self.m2m_field is not None:
                    instance.self.m2m_field.set(self.m2m_field)
                return redirect('eduAdmin', pk_key)
            return render(request,self.template_name,{'edu':edu,'form':form})
        else:
            return redirect('eduAdmin',pk_key)
        
class eduAsPk():
    def get_queryset(self):
        queryset = super().get_queryset()
        pk_key = self.kwargs.get('pk_key')
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        queryset = queryset.filter(edu=edu)
        return queryset