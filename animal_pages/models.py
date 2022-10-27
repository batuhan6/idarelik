from django.db import models
from django.utils.translation import gettext_lazy as _


class Animal(models.Model):
    animal_name = models.CharField(max_length=50, verbose_name=_("name"))

    descriptions = models.TextField(max_length=1000, verbose_name=_("descriptions"), null=True, blank=True,
                                    default="Heyy are you ready to have a new awesome friend.")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.animal_name
