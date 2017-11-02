from django.db import models
import string


class Service(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return string.capwords(self.name, '_').replace('_', ' ')


class Temperatures(models.Model):
    service_id = models.ForeignKey(Service)
    date = models.DateField()
    h_00 = models.IntegerField(default=None, null=True, blank=True)
    h_01 = models.IntegerField(default=None, null=True, blank=True)
    h_02 = models.IntegerField(default=None, null=True, blank=True)
    h_03 = models.IntegerField(default=None, null=True, blank=True)
    h_04 = models.IntegerField(default=None, null=True, blank=True)
    h_05 = models.IntegerField(default=None, null=True, blank=True)
    h_06 = models.IntegerField(default=None, null=True, blank=True)
    h_07 = models.IntegerField(default=None, null=True, blank=True)
    h_08 = models.IntegerField(default=None, null=True, blank=True)
    h_09 = models.IntegerField(default=None, null=True, blank=True)
    h_10 = models.IntegerField(default=None, null=True, blank=True)
    h_11 = models.IntegerField(default=None, null=True, blank=True)
    h_12 = models.IntegerField(default=None, null=True, blank=True)
    h_13 = models.IntegerField(default=None, null=True, blank=True)
    h_14 = models.IntegerField(default=None, null=True, blank=True)
    h_15 = models.IntegerField(default=None, null=True, blank=True)
    h_16 = models.IntegerField(default=None, null=True, blank=True)
    h_17 = models.IntegerField(default=None, null=True, blank=True)
    h_18 = models.IntegerField(default=None, null=True, blank=True)
    h_19 = models.IntegerField(default=None, null=True, blank=True)
    h_20 = models.IntegerField(default=None, null=True, blank=True)
    h_21 = models.IntegerField(default=None, null=True, blank=True)
    h_22 = models.IntegerField(default=None, null=True, blank=True)
    h_23 = models.IntegerField(default=None, null=True, blank=True)


    class Meta:
        unique_together = ('service_id', 'date')

    def get_temperatures(self):
        return [self.h_00,
                self.h_01,
                self.h_02,
                self.h_03,
                self.h_04,
                self.h_05,
                self.h_06,
                self.h_07,
                self.h_08,
                self.h_09,
                self.h_10,
                self.h_11,
                self.h_12,
                self.h_13,
                self.h_14,
                self.h_15,
                self.h_16,
                self.h_17,
                self.h_18,
                self.h_19,
                self.h_20,
                self.h_21,
                self.h_22,
                self.h_23]
