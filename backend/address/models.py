from django.db import models
from django.utils.translation import ugettext as _
from django.shortcuts import reverse
from django.conf import settings
# Create your models here.


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name='address_set'
    )
    street_address = models.CharField(_("Street"), max_length=100)
    apartment_address = models.CharField(
        _("Apartment"),
        max_length=100,
        blank=True,
        null=True
    )
    city = models.CharField(_("City"), max_length=100)
    country = models.CharField(max_length=50)
    phone = models.CharField(_("Phone"), max_length=14, blank=True, null=True)
    fax = models.CharField(_("Fax"), max_length=14, blank=True, null=True)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Address's")

    def __str__(self):
        return f"{self.user}: {self.street_address}"

    def get_absolute_url(self):
        return reverse("Address_detail", kwargs={"pk": self.pk})


class BillingAddress(models.Model):
    address = models.OneToOneField(
        "address.Address",
        verbose_name=_("Address"),
        on_delete=models.CASCADE,
        related_name="billing_address",
        blank=True, null=True
    )

    class Meta:
        verbose_name = _("BillingAddress")
        verbose_name_plural = _("BillingAddress's")

    def __str__(self):
        return self.address.__str__()

    def get_absolute_url(self):
        return reverse("BillingAddress_detail", kwargs={"pk": self.pk})


class ShippingAddress(models.Model):
    address = models.OneToOneField(
        "address.Address",
        verbose_name=_("Address"),
        on_delete=models.CASCADE,
        related_name="Shipping_address",
        blank=True, null=True
    )

    class Meta:
        verbose_name = _("ShippingAddress")
        verbose_name_plural = _("ShippingAddress's")

    def __str__(self):
        return self.address.__str__()

    def get_absolute_url(self):
        return reverse("BillingAddress_detail", kwargs={"pk": self.pk})
