from django.db import models
from django.conf import settings
from datetime import datetime


class RealTimeRate(models.Model):
    from_currency_code = models.CharField(max_length=100, blank =True, null=True,
    verbose_name="Code of the currency")
    from_currency_name = models.CharField(max_length=100, blank =True, null=True,
    verbose_name="Name of the currency")
    to_currency_code = models.CharField(max_length=100, blank =True, null=True,
    verbose_name="Code of the currency")
    to_currency_name = models.CharField(max_length=100, blank =True, null=True,
    verbose_name="Name of the currency")
    exchange_rate = models.CharField(max_length=100, blank =True, null=True,
    verbose_name="Exchange rate")
    last_refreshed = models.DateTimeField(default = datetime.now,
        verbose_name="date and time of the last refresh")
    time_zone = models.CharField(max_length=100, blank =True, null=True,
    verbose_name="Time zone")
    bid_price = models.CharField(max_length=100, blank =True, null=True,
    verbose_name="Bid price")
    ask_price = models.CharField(max_length=100, blank =True, null=True,
    verbose_name="Ask price")
    class Meta:
        verbose_name = "Rate"
        ordering = ("last_refreshed",)
        get_latest_by = ('last_refreshed',)
    def __str__(self):
        return "The exchange rate from " + str(self.from_currency_code) 
        + " to " + str(self.to_currency_code) + " is " 
        + str(self.exchange_rate) + "."
        
