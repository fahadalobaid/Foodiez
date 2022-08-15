from django.apps import AppConfig


class FoodiezappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "foodiezApp"

    def ready(self) -> None:
        import foodiezApp.signals