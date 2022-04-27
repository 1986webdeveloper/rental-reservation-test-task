# -*- coding: utf-8 -*-

"""
    reservation view
"""
import logging

from django.shortcuts import redirect, render
from django.views.generic import View

from rental_reservation.models import Rental

log = logging.getLogger(__name__)


class CommonView(View):
    """
        common view
    """
    def render_template(self, template_path, context={}):
        """
        renders template
        """
        return render(self.request, template_path, context)

#
class LoginRequiredMixin(View):
    """
        login required view
    """
    def dispatch(self, request, *args, **kwargs):
        """
            dispatch method
        """
        if not self.request.user.is_authenticated:
            return redirect("/admin")
        return super().dispatch(request, *args, **kwargs)



class HomePageView(LoginRequiredMixin, CommonView):
    """
        Homepage view
    """

    def get(self, *args, **kwargs):
        """
            Homepage view
        """
        context = {
            "rental_objs": Rental.objects.all().order_by("-id"),
        }

        return self.render_template(template_path="home.html", context=context)
