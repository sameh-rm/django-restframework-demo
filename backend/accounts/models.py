from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.utils.translation import ugettext as _
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name=_("User"), related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(
        _("Profile Picture"), upload_to="prfile_pictures", height_field=350, width_field=280)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})


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
    is_shipping_address = models.BooleanField(
        _("Is Shipping Address"), default=False)
    is_Billing_address = models.BooleanField(
        _("Is Billing Address"), default=False)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Address's")

    def __str__(self):
        return f"{self.user}: {self.street_address}"

    def get_absolute_url(self):
        return reverse("Address_detail", kwargs={"pk": self.pk})
