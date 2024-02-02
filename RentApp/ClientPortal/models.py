from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film'


class UserOrder(models.Model):
    user_order_id = models.AutoField(primary_key=True)
    orders = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_order'