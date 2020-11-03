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
