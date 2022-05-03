from django.db import models

class Factory(models.Model):
    name_factory = models.CharField(max_length=30)

class p_SvoFilm(models.Model):
    Actual_position = models.DecimalField(max_digits=19, decimal_places=10)
    Actual_speed = models.DecimalField(max_digits=19, decimal_places=10)
    Lag_error = models.DecimalField(max_digits=19, decimal_places=10)

class p_Cut(models.Model):
    Motor_Torque = models.DecimalField(max_digits=19, decimal_places=10)
    Lag_error = models.DecimalField(max_digits=19, decimal_places=10)
    Actual_position = models.DecimalField(max_digits=19, decimal_places=10)
    Actual_speed = models.DecimalField(max_digits=19, decimal_places=10)

class p_Cut_analysis(models.Model):
    speed_change = models.DecimalField(max_digits=19, decimal_places=10)
    replacement_history = models.DateTimeField(auto_now_add=True)
# Create your models here.
