from django.contrib import admin
from .models import Category, District, Division, ChandaKatha


# Register your models here.
class KothaAdmin(admin.ModelAdmin):
    list_display = ['title', 'district_name', 'division_name', 'category_name']

    class Meta:
        model = ChandaKatha


admin.site.register(ChandaKatha,KothaAdmin)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Division)
