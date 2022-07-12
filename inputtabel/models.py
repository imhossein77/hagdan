from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Inputtabel(models.Model):
    Size_C = [
        ("1", "اجتماعی فرهنگی"),
        ("2", "کشاورزی"),
        ("3", "آقتصادی")
    ]
    typer =models.CharField(_("عنوان"), max_length=100, blank=True, null=True)
    name = models.CharField(_("نام و نام خانوادگی"), max_length=60)
    phone = models.CharField(_("شماره تلفن"), max_length=14)
    email = models.EmailField(_("ایمیل"), blank=True, null=True)
    type = models.CharField(_("نوع آورده*"), max_length=50, choices=Size_C, default='1')
    photo = models.ImageField(upload_to='product/', blank=True, null=True)
    description = models.CharField(_("توضیحات"), max_length=500)
    active_rool = models.CharField(_("پذیرفتن قوانین"), max_length=200)
    active = models.BooleanField(_("نمایش"), blank=True, null=True)

    def __str__(self):
        return self.name
