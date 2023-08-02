from django.contrib.auth.models import Permission,Group
from edu_permissions.GroupsNames import GROUP_OF_INSTETUDE_HEAD,GROUP_OF_INSTETUDE_SUB_HEADS,GROUP_OF_ADMINS,GROUP_OF_STUDENTS,GROUP_OF_TEACHERS,GROUP_OF_HEAD_OF_DEPARTMENT,GROUP_OF_CLASS_INCHARGE
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

custom_permissions_flty =[
    ('can_view_edu_admin_page', 'Can View Edu Admin Page'),
    ("can_edit_edu_models", "Can Edit Edu Models"),
    ("can_create_edu_models", "Can Create Edu Models"),
    ("can_can_view_edu_models", "Can View Edu Models"),
    ("can_take_edu_online_class", "Can Take Edu Online Class"),
    ("can_take_edu_attendance", "Can Take Edu Attendance"),
    ("can_edit_edu_lvl1", "Can Edit Edu Lvl1"),
    ("can_edit_edu_lvl2", "Can Edit Edu Lvl2"),
    ("can_edit_edu_lvl3", "Can Edit Edu Lvl3"),
    ("can_change_groups_edu", "Can Change Groups Edu"),
    ("can_view_groups_edu", "Can View Groups Edu"),
    ("can_uploade_docs_for_eclass_edu", "Can Uploade Docs For Eclass Edu"),
    ("can_uploade_video_for_eclass_edu", "Can Uploade Video For Eclass Edu"),
    ("can_change_student_status_edu", "Can Change Student Status Edu"),
    ("can_approve_student_request_edu", "Can Approve Student Request Edu"),
    ("can_approve_job_request_edu", "Can Approve Job Request Edu"),
]

custom_permissions_student =[
    ("can_can_view_edu_models", "Can View Edu Models"),
    ("can_take_edu_online_class", "Can Take Edu Online Class"),
    ("can_uploade_assiment_for_eclass_edu", "Can Uploade Assiment For Eclass Edu"),
]

def create_custom_permissions_edu():
    app_models = [
        ('edu_members', 'eduFaculty'),
    ]
    for app_label, model_name in app_models:
        ModelClass = apps.get_model(app_label=app_label, model_name=model_name)
        content_type = ContentType.objects.get_for_model(ModelClass)
        for codename, name in custom_permissions_flty:
            permission, _ = Permission.objects.get_or_create(
                codename=codename,
                content_type=content_type,
                defaults={'name': name},
            )
            if permission.name != name:
                permission.name = name
                permission.save()
            
def create_custom_permissions_student():
    app_models = [
        ('edu_members', 'eduStudents'),
    ]
    for app_label, model_name in app_models:
        ModelClass = apps.get_model(app_label=app_label, model_name=model_name)
        content_type = ContentType.objects.get_for_model(ModelClass)
        for codename, name in custom_permissions_student:
            permission, _ = Permission.objects.get_or_create(
                codename=codename,
                content_type=content_type,
                defaults={'name': name},
            )
            if permission.name != name:
                permission.name = name
                permission.save()

class AddGroupToPermission:
    @staticmethod
    def admin_group():
        group, _ = Group.objects.get_or_create(name=GROUP_OF_ADMINS)
        permissions_list  = Permission.objects.filter(codename__in= [
            'can_view_edu_admin_page',
            'can_edit_edu_models',
            'can_create_edu_models',
            'can_can_view_edu_models',
            'can_view_groups_edu',
            'can_change_groups_edu',
            'can_uploade_video_for_eclass_edu',
            'can_uploade_docs_for_eclass_edu',
            'can_approve_student_request_edu',
        ])
        for permison in permissions_list:
            group.permissions.add(permison)

    @staticmethod
    def teachers_group():
        group, _ = Group.objects.get_or_create(name=GROUP_OF_TEACHERS)
        permissions_list =Permission.objects.filter(codename__in=  [
            'can_view_edu_admin_page',
            'can_can_view_edu_models',
            'can_view_groups_edu',
            'can_uploade_video_for_eclass_edu',
            'can_uploade_docs_for_eclass_edu',
        ])
        for permison in permissions_list:
            group.permissions.add(permison)

    @staticmethod
    def Students_group():
        group, _ = Group.objects.get_or_create(name=GROUP_OF_STUDENTS)
        permissions_list = Permission.objects.filter(codename__in= [
            'can_view_edu_admin_page',
            'can_can_view_edu_models',
            'can_take_edu_online_class',
        ])
        for permison in permissions_list:
            group.permissions.add(permison)

    @staticmethod
    def head_of_dept_group():
        group, _ = Group.objects.get_or_create(name=GROUP_OF_HEAD_OF_DEPARTMENT)
        permissions_list = Permission.objects.filter(codename__in=  [
            'can_view_edu_admin_page',
            'can_can_view_edu_models',
            'can_change_student_status_edu',
            'can_approve_student_request_edu',
            'can_approve_job_request_edu',
            'can_edit_edu_lvl3',
            'can_view_groups_edu',
        ])
        for permison in permissions_list:
            group.permissions.add(permison)

    @staticmethod
    def in_charge_group():
        group, _ = Group.objects.get_or_create(name=GROUP_OF_CLASS_INCHARGE)
        permissions_list = Permission.objects.filter(codename__in=  [
            'can_view_edu_admin_page',
            'can_can_view_edu_models',
            'can_change_student_status_edu',
            'can_view_groups_edu',
            'can_take_edu_attendance',
            'can_take_edu_online_class',
        ])
        for permison in permissions_list:
            group.permissions.add(permison)


    @staticmethod
    def head_group():
        group, _ = Group.objects.get_or_create(name=GROUP_OF_INSTETUDE_HEAD)
        permissions_list = Permission.objects.filter(codename__in= [
            'can_view_edu_admin_page',
            'can_edit_edu_models',
            'can_create_edu_models',
            'can_can_view_edu_models',
            'can_view_groups_edu',
            'can_change_groups_edu',
            'can_uploade_video_for_eclass_edu',
            'can_uploade_docs_for_eclass_edu',
            'can_approve_student_request_edu',
            'can_approve_job_request_edu',
            'can_change_student_status_edu',
            'can_edit_edu_lvl1',
        ])
        for permison in permissions_list:
            group.permissions.add(permison)

    @staticmethod
    def sub_head_group():
        group, _ = Group.objects.get_or_create(name=GROUP_OF_INSTETUDE_SUB_HEADS)
        permissions_list = Permission.objects.filter(codename__in=  [
            'can_view_edu_admin_page',
            'can_edit_edu_models',
            'can_create_edu_models',
            'can_can_view_edu_models',
            'can_view_groups_edu',
            'can_change_groups_edu',
            'can_uploade_video_for_eclass_edu',
            'can_uploade_docs_for_eclass_edu',
            'can_approve_student_request_edu',
            'can_approve_job_request_edu',
            'can_change_student_status_edu',
            'can_edit_edu_lvl2',
        ])
        for permison in permissions_list:
            group.permissions.add(permison)
