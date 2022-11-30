from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    fam = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    otc = models.CharField(max_length=50, null=False, blank=False)


class Images(models.Model):
    title = models.CharField(max_length=256, null=False)
    image = models.ImageField("Image")


class Coords(models.Model):
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    height = models.IntegerField(null=False, blank=False)


class Level(models.Model):
    LEVEL_CHOICES = [
        ('1А', '1А'),
        ('1Б', '1Б'),
        ('2А', '2А'),
        ('2Б', '2Б'),
        ('3А', '3А'),
        ('3Б', '3Б'),
    ]
    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, blank=True)
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, blank=True)
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, blank=True)
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, blank=True)


class Area(models.Model):
    title = models.CharField(max_length=50)


class Pereval(models.Model):
    STATUS_CHOICES = (
        (1, 'new'),
        (2, 'pending'),
        (3, 'accepted'),
        (4, 'rejected'),
    )
    image = models.ManyToManyField(Images, through='PerevalImages')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coord_id = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    area = models.ManyToManyField(Area, through='PerevalArea')
    add_time = models.DateField(auto_now_add=True)
    beautyTitle = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    other_titles = models.CharField(max_length=256, blank=True)
    connect = models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=1)


class PerevalImages(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)


class PerevalArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)




