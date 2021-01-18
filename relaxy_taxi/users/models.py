from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Relaxy Taxi."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    age = models.IntegerField(_("Возраст"), blank=True, null=True)
    phone_number = models.CharField(_("Номер телефона"), max_length=100, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name or self.username)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Driver(models.Model):
    RATING_OPTIONS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    name = models.CharField(_("Имя"), blank=True, max_length=255)
    age = models.IntegerField(_("Возраст"))
    licence_id = models.IntegerField(_("ID лицензии"))
    rating = models.IntegerField(_("Рейтинг"), choices=RATING_OPTIONS, default=RATING_OPTIONS)
    phone_number = models.CharField(_("Номер телефона"), max_length=100)

    class Meta:
        verbose_name = _("Водитель")
        verbose_name_plural = _("Водители")

    def __str__(self):
        return "%s" % (self.name or self.pk)


class Client(models.Model):
    name = models.CharField(_("Имя"), blank=True, max_length=255)
    age = models.IntegerField(_("Возраст"), blank=True, null=True)
    phone_number = models.CharField(_("Номер телефона"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Клиент")
        verbose_name_plural = _("Клиенты")

    def __str__(self):
        return "%s" % (self.name or self.pk)
