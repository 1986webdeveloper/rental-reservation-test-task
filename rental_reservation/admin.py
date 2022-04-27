from django.contrib import admin

from rental_reservation.models import (
    Rental,
    RentalReservation
)


class RentalReservationAdmin(admin.ModelAdmin):

    list_display = ["rental_id", "checkin_date", "checkout_date", "prev_reservation_id"]
    search_fields = ["rental_id__name", "checkin_date", "checkout_date"]


class RentalReservationInline(admin.TabularInline):
    model = RentalReservation
    extra = 0


class RentalAdmin(admin.ModelAdmin):

    list_display = ["name",]
    search_fields = ["name", ]
    inlines = [
        RentalReservationInline,
    ]

class RentalReservationAdmin(admin.ModelAdmin):

    list_display = ["rental_id", "checkin_date", "checkout_date", "prev_reservation_id"]
    search_fields = ["rental_id", "checkin_date", "checkout_date"]
    readonly_fields = ["prev_reservation_id", ]
    # inlines = [
    #     RentalReservationInline,
    # ]

admin.site.register(RentalReservation, RentalReservationAdmin)
admin.site.register(Rental, RentalAdmin)
