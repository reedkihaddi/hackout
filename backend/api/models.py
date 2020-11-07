from django.db import models

# Create your models here.
class TimeStampModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Location(TimeStampModel):

    class Meta:
        ordering = ['id']


    ROAD = 'RD'
    STREETLIGHT = 'SL'
    PUBLICWASHROOM = 'PW'
    SEWAGE = 'SW'
    GARBAGE = 'GB'
    OTHER = 'OR'
    CHOICES = [
        (ROAD, 'Road'),
        (STREETLIGHT, 'StreetLight'),
        (PUBLICWASHROOM, 'PublicWashroom'),
        (SEWAGE, 'Sewage'),
        (GARBAGE, 'Garbage'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.IntegerField(default=1, blank=True)
    upvotes = models.IntegerField(blank=True, default=0)
    variant = models.CharField(max_length=2, choices=CHOICES, default="RD")
    pic = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Longitude:{} Latitude:{}'.format(self.longitude, self.latitude)

