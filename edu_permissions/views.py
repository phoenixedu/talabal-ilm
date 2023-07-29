from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View,ListView
from .models import HeadOfTheDepartment, GroupOfAdmins, GroupOfSubHeadOfInstetude, GroupOfStudents, GroupOfTeachers, InchargeOfClass, HeadOfInstetude
from edu.models import xEduInstitution
from edu_members.models import eduFaculty
# Create your views here.
class AllGroupsView(View):
    template_name = "groups/allGroups.html"

    def get(self, request, pk_key):
        edu = get_object_or_404(xEduInstitution, pk_key=pk_key)
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
    def post(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        teachGp = GroupOfTeachers.objects.get(edu=edu)
        admin_group = GroupOfAdmins.objects.get(edu=edu)
        head_dpt = HeadOfTheDepartment.objects.filter(edu=edu)
        class_incharge = InchargeOfClass.objects.filter(edu=edu)
        sub_head_edu = GroupOfSubHeadOfInstetude.objects.get(edu=edu)
        head_edu = HeadOfInstetude.objects.get(edu=edu)

        memberID = request.POST.get('member_id')
        sub = request.POST.get('sub')
        action = request.POST.get('action')
        if request.POST:
            try:
                if action == "rm_teacher":
                    teachGp.members.remove(memberID)
                elif action == "rm_admin":
                    admin_group.members.remove(memberID)
                elif action == "rm_sub_head":
                    sub_head_edu.members.remove(memberID)
                elif action == "rm_head":
                    head_edu.members.remove(memberID)
                elif action == "rm_hod":
                    for i in head_dpt:
                        if i.department == sub:
                            i.members.remove(memberID)
                elif action == "rm_cls":
                    for i in class_incharge:
                        if i.Eclass == sub:
                            i.members.remove(memberID)
                return redirect(request.path)
            except Exception as e:
                print(f"Error: {e}")
                pass
        else:
            print('not work')
        
        contx ={
            'edu':edu,
        }
        return render(request,self.template_name,contx)

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
            print(f"error: {e}")
            pass
        contx ={
            self.group: group,
            self.members : members,
            self.context_object_name : users,
            'edu':edu,
        }
        return render(request,self.template_name,contx)
    
    def post(self,request,name,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        users = eduFaculty.objects.filter(
            edu=edu,
            ex_Faculty=False,
            disable=False,
            suspend=False,
        )
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
            print(f"error: {e}")
            pass
        if action == "add":
            group.members.add(memberID)
            print(f"member {memberID} is added to {group.name}")
        contx ={
            self.group: group,
            self.members : members,
            self.context_object_name : users,
            'edu':edu,
        }
        return render(request,self.template_name,contx)
