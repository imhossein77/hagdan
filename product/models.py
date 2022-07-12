from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Product(models.Model):
    Color_C = [
        ("1", "شماره 1"),
        ("2", "شماره2"),
        ("3", "شماره 3"),
        ("4", "شماره 4"),
        ("5", "شماره 5"),
        ("6", "شماره 6"),
        ("7", "شماره 7"),
        ("8", "شماره 8")
    ]
    Title_C = [
        ("شاهانی", "شاهانی"),
        ("خاصویی", "خاصویی"),
        ("زاهدی", "زاهدی")
    ]
    Size_C = [
        ("1", "درشت"),
        ("2", "متوسط"),
        ("3", "ریز")
    ]
    points = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    name = models.CharField(_("نام و نام خانوادگی"), max_length=100)
    phone = models.CharField(_("شماره تلفن"), max_length=20)
    Product_tonnage = models.CharField(_("تناژ محصول (به واحد تناژ)"), max_length=20)
    Crop_location = models.CharField(_("محل کشت محصول*"), max_length=100)
    size = models.CharField(_("سایز خرمای شما (به سانت)*"), max_length=20, choices=Size_C, default='1')
    price = models.CharField(_("قیمت محصول"), max_length=20)
    Around_the_harvest_date = models.CharField(_("حدود تاریخ برداشت"), max_length=20)
    date_type = models.CharField(_("نوع خرما*"), max_length=50, choices=Title_C, default='1')
    color_type = models.CharField(_("رنگ خرما (طبق جدول استاندارد)"), max_length=50, choices=Color_C, default='زاهدی')
    photo = models.ImageField(upload_to='product/')
    description = models.CharField(_("توضیحات"), max_length=500)
    colorr = models.CharField(_("انتخاب رنگ"), max_length=200)
    active_rool = models.CharField(_("پذیرفتن قوانین"), max_length=200)
    active = models.BooleanField(_("نمایش"), blank=True, null=True)
    category = models.ForeignKey('Category', related_name="product", verbose_name=_('دسته بندی'),
                                 on_delete=models.CASCADE
                                 , blank=True, null=True)
    points_op = models.IntegerField(_("امتیاز"), choices=points, blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=200)
    phone = models.CharField(_("تلفن"), max_length=15)
    description = models.CharField(_("توضیحات"), max_length=200)

    def __str__(self):
        return self.phone


class Category(models.Model):
    titel = models.CharField(_('عنوان'), max_length=50)
    type = models.SlugField(_('نام لاتین'))

    def __str__(self):
        return self.titel


class RegPrice(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=100)
    phone = models.CharField(_("شماره تلفن"), max_length=20)
    email = models.EmailField(_("Email"), blank=True, null=True)
    Product_tonnage = models.CharField(_("تناژ محصول (به واحد تناژ)"), max_length=20)
    active_rool = models.CharField(_("پذیرفتن قوانین"), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Product_tonnage
