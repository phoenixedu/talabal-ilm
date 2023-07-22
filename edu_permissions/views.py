from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from .models import HeadOfTheDepartment, GroupOfAdmins, GroupOfSubHeadOfInstetude, GroupOfStudents, GroupOfTeachers, InchargeOfClass, HeadOfInstetude
from edu.models import xEduInstitution
# Create your views here.
class groupsView(View):
    template_name = "groups/allGroups.html"
    def get(self,request,pk_key):
        edu = get_object_or_404(xEduInstitution,pk_key=pk_key)
        headGp = HeadOfInstetude.objects.get(edu=edu)
        # head_dpt = HeadOfTheDepartment.objects.filter(edu=edu)
        # adminsGp = GroupOfAdmins.objects.get(edu=edu)
        # sub_heads = GroupOfSubHeadOfInstetude.objects.get(edu=edu)
        # teachersGp = GroupOfTeachers.objects.get(edu=edu)
        # studentsGp = GroupOfStudents.objects.get(edu=edu)
        # classIncharge = InchargeOfClass.objects.filter(edu=edu)
        contx = {
            'edu': edu,
            'groups': {
                'Head Group': headGp,
                # 'Head of the Department': head_dpt,
                # 'Admins Group': adminsGp,
                # 'Sub Heads': sub_heads,
                # 'Teachers Group': teachersGp,
                # 'Students Group': studentsGp,
                # 'Class Incharge': classIncharge,
            }
        }
        return render(request,self.template_name,contx)