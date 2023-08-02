from django.apps import AppConfig


class EduPermissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu_permissions'

    def ready(self):
        import edu_permissions.signal
        from edu_permissions.permissions import create_custom_permissions_edu,create_custom_permissions_student,AddGroupToPermission
        create_custom_permissions_edu()
        create_custom_permissions_student()
        AddGroupToPermission.admin_group()
        AddGroupToPermission.head_group()
        AddGroupToPermission.head_of_dept_group()
        AddGroupToPermission.in_charge_group()
        AddGroupToPermission.Students_group()
        AddGroupToPermission.sub_head_group()
        AddGroupToPermission.teachers_group()