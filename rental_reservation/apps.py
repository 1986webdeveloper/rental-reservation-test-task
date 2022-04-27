from django.apps import AppConfig


class RentalReservationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rental_reservation'

    def ready(self):
        """On App Configuration add signal for same also"""
        import rental_reservation.signals