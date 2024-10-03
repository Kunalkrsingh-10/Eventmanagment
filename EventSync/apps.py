from django.apps import AppConfig


class EventsyncConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "EventSync"
    def ready(self):
        import EventSync.Signal
