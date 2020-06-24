from django.contrib import admin
from home.models import HomeImage, WebMeta


# @admin.register(Home)
# class HomeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'home_image', 'is_banner', 'is_card')


@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_banner', 'is_card', 'index', 'title', 'text')


@admin.register(WebMeta)
class WebMetaAdmin(admin.ModelAdmin):
    list_display = ('title', 'seo_desc', 'seo_key', 'is_use', 'pub_date')