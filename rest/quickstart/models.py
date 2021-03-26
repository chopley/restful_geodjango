from django.contrib.gis.db import models


class Sensor(models.Model):
    """
    Represents a Sensor
    """
    name = models.CharField(max_length=200, null=True, blank=True)
    imei = models.CharField(max_length=200, null=True, blank=True)


class SensorData(models.Model):
    """
    Represents a single Sensor datapoint
    """
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE,)
    date = models.DateTimeField()
    # swell size in feet
    co2_sensor = models.FloatField()
    location = models.PointField()
    battery_voltage_main = models.FloatField()
    battery_voltage_secondary = models.FloatField()

    @property
    def lat_lng(self):
        return list(getattr(self.location, 'coords', [])[::-1])


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    imei = models.CharField(max_length=30)
    co2_sensor = models.FloatField()
    battery_voltage_main = models.FloatField()
    battery_voltage_secondary = models.FloatField()


#https://stackoverflow.com/questions/58941819/django-database-structure-for-time-series-data