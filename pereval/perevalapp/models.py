from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    fam = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    otc = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.fam}'


class Image(models.Model):
    title = models.CharField(max_length=256, null=False)
    image = models.ImageField("Image", upload_to='media/')


class Coords(models.Model):
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    height = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Area(models.Model):
    title = models.CharField(max_length=50)


class Pereval(models.Model):
    STATUS_CHOICES = (
        (1, 'new'),
        (2, 'pending'),
        (3, 'accepted'),
        (4, 'rejected'),
    )
    LEVEL_CHOICES = (
        (1, '1А'),
        (2, '1Б'),
        (3, '2А'),
        (4, '2Б'),
        (5, '3А'),
        (6, '3Б'),
    )
    image = models.ManyToManyField(Image, through='PerevalImages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord_id = models.ForeignKey(Coords, on_delete=models.CASCADE)
    area = models.ManyToManyField(Area, through='PerevalArea')
    add_time = models.DateField(auto_now_add=True)
    beautyTitle = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    other_titles = models.CharField(max_length=256, blank=True)
    connect = models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=1)
    level_winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, default="", blank=True)
    level_spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, default="", blank=True)
    level_summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, default="", blank=True)
    level_autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, default="", blank=True)


class PerevalImages(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)


class PerevalArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)




