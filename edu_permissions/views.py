from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View,ListView
from .models import HeadOfTheDepartment, GroupOfAdmins, GroupOfSubHeadOfInstetude, GroupOfStudents, GroupOfTeachers, InchargeOfClass, HeadOfInstetude
from edu.models import xEduInstitution
from edu_members.models import eduFaculty
from django.contrib import messages
# Create your views here.

class AllGroupsView(View):
    template_name = "groups/allGroups.html"
    def get(self, request, pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
        if request.user.has_perm('edu_members.can_view_groups_edu'):
            teachGp,_ = GroupOfTeachers.objects.get_or_create(edu=edu)
            admin_group,_ = GroupOfAdmins.objects.get_or_create(edu=edu)
            head_dpt = HeadOfTheDepartment.objects.filter(edu=edu)
            class_incharge = InchargeOfClass.objects.filter(edu=edu)
            sub_head_edu,_ = GroupOfSubHeadOfInstetude.objects.get_or_create(edu=edu)
            head_edu,_ = HeadOfInstetude.objects.get_or_create(edu=edu)
            context = {
                'teach_group': teachGp,
                'adm_group': admin_group,
                'dpt_head': head_dpt,
                'class_incharge': class_incharge,
                'sub_head': sub_head_edu,
                'edu_head': head_edu,
                'edu':edu,
            } 
            return render(request, self.template_name, context)
        else:
            return redirect('eduAdmin' , pk_key=edu.pk_key)
    def post(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        teachGp = GroupOfTeachers.objects.get(edu=edu)
        admin_group = GroupOfAdmins.objects.get(edu=edu)
        head_dpt = HeadOfTheDepartment.objects.filter(edu=edu)
        class_incharge = InchargeOfClass.objects.filter(edu=edu)
        sub_head_edu = GroupOfSubHeadOfInstetude.objects.get(edu=edu)
        head_edu = HeadOfInstetude.objects.get(edu=edu)
        if request.user.has_perm('edu_members.can_change_groups_edu'):
            memberID = request.POST.get('member_id')
            sub = request.POST.get('sub')
            action = request.POST.get('action')
            if request.POST:
                try:
                    if action == "rm_teacher":
                        teachGp.members.remove(memberID)
                        teachGp.save()
                    elif action == "rm_admin":
                        admin_group.members.remove(memberID)
                        admin_group.save()
                    elif action == "rm_sub_head":
                        sub_head_edu.members.remove(memberID)
                        sub_head_edu.save()
                    elif action == "rm_head":
                        head_edu.members.remove(memberID)
                        head_edu.save()
                    elif action == "rm_hod":
                        for i in head_dpt:
                            if i.department.id == int(sub):
                                i.members.remove(memberID)
                                i.save()
                    elif action == "rm_cls":
                        for i in class_incharge:
                            if i.Eclass.id == int(sub):
                                i.members.remove(memberID)
                                i.save()
                    return redirect(request.path)
                except Exception as e:
                    messages.error(request, f"Error: {e}")
                    pass
            contx ={
                'edu':edu,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('eduAdmin' , pk_key=edu.pk_key)

class listForHOD(ListView):
    model = eduFaculty
    template_name = "groups/addlist.html"
    context_object_name = "add_list"
    def get(self,request,name,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        group = get_object_or_404(HeadOfTheDepartment,name=name,edu=edu)
        users = eduFaculty.objects.filter(
            edu=edu,
            ex_Faculty=False,
            disable=False,
            suspend=False,
        )
        members = group.members.all()
        if request.user.has_perm('edu_members.can_change_groups_edu'):
            contx ={
                'edu':edu,
                'group':group,
                'members':members,
                self.context_object_name:users,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('eduAdmin' , pk_key=edu.pk_key)
    
    def post(self,request,name,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        group = get_object_or_404(HeadOfTheDepartment,name=name,edu=edu)
        users = eduFaculty.objects.filter(
            edu=edu,
            ex_Faculty=False,
            disable=False,
            suspend=False,
        )
        if request.user.has_perm('edu_members.can_change_groups_edu'):
            memberID = request.POST.get('member_id')
            action = request.POST.get('action')
            if action == "add":
                group.members.add(memberID)
                group.save()
                dpt = group.department
                return redirect('departmentD' , pk_key=pk_key, name=dpt.name,pk=dpt.pk)
            contx ={
                'edu':edu,
                'group':group,
                self.context_object_name:users,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('eduAdmin' , pk_key=edu.pk_key)

class addListOfFlty(ListView):
    model = eduFaculty
    template_name = "groups/addlist.html"
    context_object_name = "add_list"
    members = "members"
    group = "group"
    def get(self,request,name,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        users = eduFaculty.objects.filter(
            edu=edu,
            ex_Faculty=False,
            disable=False,
            suspend=False,
        )
        if request.user.has_perm('edu_members.can_change_groups_edu'):
            try: 
                try:
                    group = GroupOfTeachers.objects.get(edu=edu, name=name)
                    members = group.members.all()
                except GroupOfTeachers.DoesNotExist:
                    try:
                        group = GroupOfAdmins.objects.get(edu=edu, name=name)
                        members = group.members.all()
                    except GroupOfAdmins.DoesNotExist:
                        try:
                            group = GroupOfSubHeadOfInstetude.objects.get(edu=edu, name=name)
                            members = group.members.all()
                        except GroupOfSubHeadOfInstetude.DoesNotExist:
                            try:
                                group = HeadOfInstetude.objects.get(edu=edu, name=name)
                                members = group.members.all()
                            except HeadOfInstetude.DoesNotExist:
                                raise ValueError("Invalid group name!")
            except Exception as e:
                messages.error(request, f"Error: {e}")
                pass
            contx ={
                self.group: group,
                self.members : members,
                self.context_object_name : users,
                'edu':edu,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('eduAdmin' , pk_key=edu.pk_key)
    
    def post(self,request,name,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        users = eduFaculty.objects.filter(
            edu=edu,
            ex_Faculty=False,
            disable=False,
            suspend=False,
        )
        if request.user.has_perm('edu_members.can_change_groups_edu'):
            memberID = request.POST.get('member_id')
            action = request.POST.get('action')
            try: 
                try:
                    group = GroupOfTeachers.objects.get(edu=edu, name=name)
                    members = group.members.all()
                except GroupOfTeachers.DoesNotExist:
                    try:
                        group = GroupOfAdmins.objects.get(edu=edu, name=name)
                        members = group.members.all()
                    except GroupOfAdmins.DoesNotExist:
                        try:
                            group = GroupOfSubHeadOfInstetude.objects.get(edu=edu, name=name)
                            members = group.members.all()
                        except GroupOfSubHeadOfInstetude.DoesNotExist:
                            try:
                                group = HeadOfInstetude.objects.get(edu=edu, name=name)
                                members = group.members.all()
                            except HeadOfInstetude.DoesNotExist:
                                raise ValueError("Invalid group name!")
            except Exception as e:
                messages.error(request, f"Error: {e}")
                pass
            if action == "add":
                group.members.add(memberID)
                group.save()
            contx ={
                self.group: group,
                self.members : members,
                self.context_object_name : users,
                'edu':edu,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('eduAdmin' , pk_key=edu.pk_key)
