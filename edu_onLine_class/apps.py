from django.apps import AppConfig


class EduOnlineClassConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu_onLine_class'

    def ready(self):
        import edu_onLine_class.signal # noqa: F401