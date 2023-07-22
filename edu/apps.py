from django.apps import AppConfig


class EduConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu'

    def ready(self):
        import edu.signal
