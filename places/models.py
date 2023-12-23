from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=200, blank=True)
    description_long = models.TextField(blank=True)
    coordinates_lng = models.DecimalField(max_digits=17, decimal_places=14,
                                          blank=True)
    coordinates_lat = models.DecimalField(max_digits=16, decimal_places=14,
                                          blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    place = models.ForeignKey(Place, related_name='image',
                              on_delete=models.DO_NOTHING)
    position = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.position} {self.place.title}'

    class Meta:
        ordering = ['place', '-position']
