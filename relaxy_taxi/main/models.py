from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    owner = models.ForeignKey("users.Driver", on_delete=models.CASCADE, related_name="cars", verbose_name=_("Владелец"))
    brand = models.CharField(_("Марка"), max_length=100)
    released_at = models.DateTimeField(_("Дата выпуска"))

    class Meta:
        verbose_name = _("Автомобиль")
        verbose_name_plural = _("Автомобили")

    def __str__(self):
        return f""


class Order(models.Model):
    NEW = 10
    PROCESSING = 20
    DONE = 30
    CANCELED = 40

    STATUS_OPTIONS = (
        (NEW, _("Новый")),
        (PROCESSING, _("В обработке")),
        (DONE, _("Выполнен")),
        (CANCELED, _("Отменён")),
    )
    status = models.IntegerField(_("Статус"), choices=STATUS_OPTIONS, default=NEW)

    client = models.ForeignKey("users.User", on_delete=models.SET_NULL, related_name="orders", null=True,
                               verbose_name=_("Клиент"))
    driver = models.ForeignKey("users.Driver", on_delete=models.SET_NULL, related_name="orders", null=True,
                               verbose_name=_("Водитель"))
    car = models.ForeignKey("main.Car", on_delete=models.SET_NULL, related_name="orders", null=True,
                            verbose_name=_("Автомобиль"))
    address = models.CharField(_("Адресс пункта назначения"), max_length=100)

    client_comment = models.TextField(_("Комментарий клиента"), blank=True, null=True)
    driver_comment = models.TextField(_("Комментарий водителя"), blank=True, null=True)

    created_at = models.DateTimeField(_("Время создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Время обновления"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __str__(self):
        return f"Заказ #{self.pk}"
