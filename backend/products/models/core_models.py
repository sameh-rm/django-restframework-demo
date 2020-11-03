from django.db import models
from django.utils.translation import ugettext as _
from django.shortcuts import reverse
from django.conf import settings
# Create your models here.
# Product, Category, Unit,
# Supplier
# Customer
# Images
# Log Table => {TableName:"Product", Action:"Insert", User:"Sameh",
# Date:"03/11/2020 12:45 PM", Message:"<Product id:1 name:Product1> has been inserted successfully by sameh at 03/11/2020 12:45PM ", targetID:1 }


class Product(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name=_(""), on_delete=models.CASCADE)
    brand = models.CharField(_("Brand Name"), max_length=50)   # Sha3rawy
    model = models.CharField(_("Model Name"), max_length=50)   # Egyptian
    # Oxidized Double Kamanja
    name = models.CharField(_("Product Name"), max_length=255)
    sku = models.CharField(_("SKU"), max_length=50)  # SH-001-EGY-001-ODK
    # TODO: Implement Auto Generated SKU
    barcode = models.CharField(_("Barcode"), max_length=50)  # if existed
    price = models.FloatField(_("Price"), default=0)
    quantity = models.IntegerField(_("Current Quantity"), default=0)
    height = models.FloatField(_("Height"), default=0)
    weight = models.FloatField(_("Weight"), default=0)
    vat = models.FloatField(_("Value-Added Tax"))
    starting_balance = models.IntegerField(_("Starting Balance"))
    # TODO:to be implemented int the future
    # lifo_fifo = models.TextField(
    #     _(""), choices=[("FIFO", "First In First Out"), ("LIFO", "Last In First Out")])

    is_active = models.BooleanField(_("IsActive"), default=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


class Variant(models.Model):
    name = models.CharField(_("Variant Name"), max_length=50)

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Variant_detail", kwargs={"pk": self.pk})

    @property
    def get_options(self):
        return self.options.all()


class VariantOption(models.Model):
    variant = models.ForeignKey(
        "products.Variant",
        related_name='options',
        verbose_name=_("Variant"),
        on_delete=models.CASCADE
    )
    detail = models.CharField(_("Variant Detail"), max_length=100)

    class Meta:
        verbose_name = _("VariantOption")
        verbose_name_plural = _("VariantOptions")

    def __str__(self):
        return f'{self.variant.name}: {self.detail}'

    def get_absolute_url(self):
        return reverse("VariantOption_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=50)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Image(models.Model):
    product = models.ForeignKey("products.Product", verbose_name=_(
        "Product"), related_name='images', on_delete=models.CASCADE)
    img = models.ImageField(_("Image"), upload_to="product-images",)
    title = models.CharField(_("Title"), max_length=100)
    alt = models.CharField(_("Alt"), max_length=100)
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return f'{self.product.name}: {self.title}'

    def get_absolute_url(self):
        return reverse("Image_detail", kwargs={"pk": self.pk})

    @property
    def img_url(self):
        if self != None:
            return self.url
        else:
            return None


class OfferPlan(models.TextChoices):
    """
    Choices to detect which field to check 
    """
    QUANTITY = "quantity", _("Quantity")
    TOTAL = "sub_total", _("Total")


class OfferType(models.TextChoices):
    """
    Choices for the types of the applied valued discount, percentage discount or gift
    """
    GIFT = "gift", _("Gift")
    VALUE = "valued_discount", _("Value")
    PERCENTAGE = "percentage_discount", _("Percentage")


class OfferTimes(models.TextChoices):
    """
    Choices for how many time should the the application
    apply an offer on a specific Product

    """
    ONCE = ("ONCE", _("Apply offer one time per order"))
    FOREACH = ("FOREACH", _("Each time customer reach's the target Apply Offer"))
    FOR_X = ("FOR_X", _("Apply offer for X times on the same order"))
    LIMITED = ("LIMITED", _("Apply offer once per order for X times"))


class Offer(models.Model):
    product = models.ForeignKey("products.Product", verbose_name=_(
        "Product"), related_name="offers", on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=60)
    plan = models.CharField(
        _("Offer Plan"),
        choices=OfferPlan.choices,
        default=OfferPlan.QUANTITY,
        max_length=10
    )
    target = models.DecimalField(
        _("Offer Target"), max_digits=8, decimal_places=2, default=0)

    offer_type = models.CharField(
        _("Target Type"),
        choices=OfferType.choices,
        default=OfferType.GIFT,
        max_length=20
    )
    offer_times = models.CharField(
        _("Target Type"),
        choices=OfferTimes.choices,
        default=OfferTimes.ONCE,
        max_length=50
    )
    reward = models.DecimalField(
        _("Reward"), max_digits=8, decimal_places=2, default=0)
    offer_max_times = models.PositiveIntegerField(_("Offer Limit"), default=0)
    orders_count = models.PositiveIntegerField(
        _("Number Of Orders"), default=0)
    remaining_orders = models.PositiveIntegerField(
        _("Remaining Orders"), default=0)

    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Offer_detail", kwargs={"pk": self.pk})

    def apply_offer(self, item):
        return self._apply_apply_offer(item)

    def _apply_apply_offer(self, item):
        attr = getattr(item, self.plan)
        print(attr)
        if attr >= self.target:
            if self.offer_times == OfferTimes.ONCE:
                # applying once setting the targeted attribute
                # to the value of the offer
                setattr(item, self.offer_type, self.reward)
                return True
            elif self.offer_times == OfferTimes.LIMITED:
                # check if the remaining orders count > 0
                # then applying the order once
                # if offer_type was gift and the target was 10 value is 2
                # then the item.gift = 2
                if self.remaining_orders > 0:
                    setattr(item, self.offer_type, self.reward)
                    self.remaining_orders -= 1
                    self.save()
                    return True
            elif self.offer_times == OfferTimes.FOR_X:
                if self.offer_max_times > 0:
                    times_to_apply = getattr(item, self.plan) // self.target
                    if times_to_apply < self.offer_max_times:
                        offer_value = self.reward * times_to_apply
                    else:
                        offer_value = self.reward * self.offer_max_times
                    # setting the offer value on the targeted item attribute
                    # depends on offer plan
                    # if GIFT => gift
                    # if PERCENTAGE  => percentage_discount
                    # if VALUE  => valued_discount
                    setattr(item, self.offer_type, offer_value)
                    return True
            elif self.offer_times == OfferTimes.FOREACH:
                times_to_apply = getattr(item, self.plan) // self.target
                reward = times_to_apply * self.reward
                print(reward)
                if not self.offer_type == OfferType.PERCENTAGE:
                    print(self.offer_type)
                    setattr(item, self.offer_type, reward)
                    return True
                else:
                    # percentage is diffrent since 5% always the right value
                    setattr(item, self.offer_type, self.reward)
                    return True

            return False
