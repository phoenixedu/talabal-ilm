from django.apps import AppConfig


class EduPermissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu_permissions'

    def ready(self):
        import edu_permissions.signal