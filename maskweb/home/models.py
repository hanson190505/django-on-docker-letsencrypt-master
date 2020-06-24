from django.db import models


class HomeImage(models.Model):
    home_image = models.ImageField(upload_to='static/home/%Y/%m/%d')
    name = models.CharField(max_length=32)
    is_banner = models.BooleanField(default=False)
    is_card = models.BooleanField(default=False)
    index = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    text = models.CharField(max_length=128, blank=True, null=True)


class WebMeta(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    seo_desc = models.CharField(max_length=256, blank=True, null=True)
    seo_key = models.CharField(max_length=128, blank=True, null=True)
    is_use = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
