# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver

from rental_reservation.models import RentalReservation


@receiver(post_save, sender=RentalReservation)
def assign_prev_reservation(sender, instance, **kwargs):
    """
        Assign prev reservation 
    """
    if "created" in kwargs and kwargs.get("created"):

        reservation_obj = RentalReservation.objects.filter(rental_id=instance.rental_id).order_by("-id")

        if len(reservation_obj) >= 2:
            instance.prev_reservation_id = reservation_obj[1]
            instance.save()
