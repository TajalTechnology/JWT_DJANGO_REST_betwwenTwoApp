from django.db import models


# Create your models here.
class Common(models.Model):
    name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Division(Common):
    pass


class District(Common):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    lat = models.CharField(max_length=200, default=None, null=True)
    lon = models.CharField(max_length=200, default=None, null=True)


class Category(Common):
    pass


class ChandaKatha(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def category_name(self):
        return self.category.name

    def district_name(self):
        return self.district.name

    def division_name(self):
        return self.district.division.name


class JWTPayloadTrack(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    iat = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'JWT Payload Tracks'

    def __str__(self):
        return self.username
