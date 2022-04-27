# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.exceptions import ValidationError


class Rental(models.Model):
    """
        Rental Modal, which manage Rental
    """

    name = models.CharField(verbose_name="Rental Name", max_length=255)

    def __str__(self):
        # import pdb;pdb.set_trace()
        return self.name


class RentalReservation(models.Model):
    """
        Rental Reservation Management
    """

    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkout_date = models.DateField(verbose_name="Checkout Date", auto_created=True)
    checkin_date = models.DateField(verbose_name="Checkin Date", auto_created=True)
    prev_reservation_id = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        # import pdb;pdb.set_trace()
        return "Res- " + str(self.id) if self else "-"

    class Meta:
        ordering = ["id", ]

    def clean(self):
        # Check that the checkin date is less than todays date?
        if self.checkin_date and self.checkin_date < datetime.datetime.today().date():
            raise ValidationError("Checkin date is must be greater than or equal to todays date...")

        # Check, checkoutdate is less than todays date?
        if self.checkout_date and self.checkout_date < datetime.datetime.today().date():
            raise ValidationError("Checkout date is must be greater than or equal to todays date...")
        
        # Check, Checkout date is must be greater than checkin date
        if self.checkin_date > self.checkout_date:
            raise ValidationError("Checkout date is must be greater than Checkin date...")

        # # Check, 
        # if self.checkout_date < self.checkin_date:
        #     raise ValidationError("Checkin date is must be less than Checkout date...")
