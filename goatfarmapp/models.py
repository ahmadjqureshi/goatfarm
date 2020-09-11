from django.db import models


# Create your models here.


class AnimalType(models.Model):
    TypeID = models.PositiveIntegerField()
    TypeName = models.CharField(max_length=64)


class City(models.Model):
    CityID = models.PositiveIntegerField()
    CityName = models.CharField(max_length=64)


class Breed(models.Model):
    BreedID = models.PositiveIntegerField()
    AnimalTypeFK = models.ForeignKey(AnimalType, on_delete=models.CASCADE, )
    BreedName = models.CharField(max_length=64)
    BreedDescription = models.CharField(max_length=1024)


class AnimalData(models.Model):
    AnimalID = models.PositiveIntegerField(blank=False,)
    AnimalTypeFK = models.ForeignKey(AnimalType, on_delete=models.CASCADE, )
    BreedFK = models.ForeignKey(Breed, on_delete=models.CASCADE, )
    CityFK = models.ForeignKey(City, on_delete=models.CASCADE, )
    Heading = models.CharField(max_length=256, blank=False,)
    Description = models.CharField(max_length=1024, blank=False)
    Price = models.FloatField(blank=False)
    Height = models.FloatField()
    Length = models.FloatField()
    neckCircumference = models.FloatField()


class AnimalPicture(models.Model):
    PicID = models.PositiveIntegerField(blank=False, )
    AnimalID = models.ForeignKey(AnimalData, on_delete=models.CASCADE, blank=False,)
    PicFileName = models.CharField(max_length=1024)
    ThumbNailName = models.CharField(max_length=1024)
