from django.db import models


class Suppliers(models.Model):
    s_name = models.CharField(max_length=64)
    s_addr = models.CharField(max_length=128, blank=True, null=True)
    s_manager = models.CharField(max_length=32, blank=True, null=True)
    s_contact = models.CharField(max_length=32)
    s_email = models.EmailField()
    s_mobile = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.s_name


class Category(models.Model):
    item = models.CharField('产品大类', max_length=64, unique=True)
    item_child = models.CharField('产品子类', max_length=64, blank=True, null=True)
    pub_date = models.DateTimeField('提交日期', auto_now_add=True)

    def __str__(self):
        return self.item + self.item_child


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='产品类别')
    pro_name = models.CharField('产品名称', max_length=32, default='mask')
    pro_desc = models.CharField('seo描述', max_length=128, blank=True, null=True)
    pro_keywords = models.CharField('seo关键词', max_length=128, blank=True, null=True)
    pro_type = models.CharField('规格型号', max_length=32, default='None')
    pro_supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, verbose_name='供应商')
    pro_price = models.DecimalField('产品单价($)', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.pro_name


class ProductDetail(models.Model):
    is_cover = models.BooleanField('是否封面', default=False)
    name = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='产品名称')
    image = models.ImageField(upload_to='mediafiles/product/%Y/%m/%d')
