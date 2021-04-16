from django.apps import AppConfig


class VillappConfig(AppConfig):
    name = 'villapp'

    def ready(self):
        import villapp.signals
