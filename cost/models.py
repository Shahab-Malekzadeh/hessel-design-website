from django.db import models


class ComponentCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام دسته بندی ')
    price = models.FloatField(verbose_name='قیمت هر واحد (به تومان) ')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی اجزا'
        verbose_name_plural = 'دسته بندی اجزا'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} - {self.price} تومان '


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام محصول ')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات محصول')
    product_image = models.ImageField(
        upload_to='images/product/', blank=True, null=True,
        verbose_name='تصویر محصول ')
    no_prod_per_year = models.IntegerField(
        verbose_name='چه تعداد از این محصول در سال تولید می شود')
    components_cost = models.IntegerField(
        default=0,
        blank=True, null=True,
        verbose_name='هزینه ی اجزای تشکیل شده (به تومان) ')
    current_expense = models.IntegerField(
        default=0,
        blank=True, null=True,
        verbose_name='هزینه های جاری برای این محصول (به تومان) ')
    profit_percent = models.IntegerField(
        default=0,
        blank=True, null=True,
        verbose_name='سود این محصول ( به درصد % ) ')
    final_price = models.IntegerField(
        default=0,
        blank=True, null=True,
        verbose_name='قیمت نهایی (به تومان) ')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        components_cost = 0 if self.components_cost is None else self.components_cost
        current_expense = 0 if self.current_expense is None else self.current_expense
        profit_percent = 0 if self.profit_percent is None else self.profit_percent
        price = components_cost + current_expense
        self.final_price = int(price * profit_percent / 100) + price
        super().save(*args, **kwargs)


class Component(models.Model):
    category = models.ForeignKey(
        ComponentCategory, on_delete=models.CASCADE,
        verbose_name='از کدام نوع دسته بندی است ')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='برای چه محصولی است ')
    name = models.CharField(max_length=200, verbose_name='نام این جزء ')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات ')
    component_image = models.ImageField(
        upload_to='images/component/', blank=True, null=True,
        verbose_name='تصویر اجزا ')
    used_count = models.IntegerField(verbose_name='چه تعداد از این جزء استفاده می شود ')
    per_product = models.IntegerField(verbose_name='برای چه تعداد از محصول انتخاب شده ')

    class Meta:
        verbose_name = 'اجزا'
        verbose_name_plural = 'اجزا'
        ordering = ['id']

    def __str__(self):
        return self.name


class ComponentConstant(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام ')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات ')
    component_constant_image = models.ImageField(
        upload_to='images/component_constant/', blank=True, null=True,
        verbose_name='تصویر اجزا ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                verbose_name='برای چه محصولی است ')
    price = models.FloatField(verbose_name='قیمت ')
    per_product = models.IntegerField(verbose_name='برای چه تعداد از محصول انتخاب شده ')

    class Meta:
        verbose_name = 'اجزای ثابت'
        verbose_name_plural = 'اجزای ثابت'
        ordering = ['id']

    def __str__(self):
        return self.name


class CurrentExpense(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام ')
    cost_in_a_year = models.IntegerField(verbose_name='هزینه در یک سال (به تومان) ')

    class Meta:
        verbose_name = 'هزینه جاری'
        verbose_name_plural = 'هزینه های جاری'
        ordering = ['id']


class TutorialVideo(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField()


from .signals import *
