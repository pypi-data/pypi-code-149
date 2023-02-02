import datetime

from django import template

from commons.python import formatter, utils

register = template.Library()


@register.filter(name='decimalf')
def format_decimal(val, decimal_places=2):
    return formatter.decimal(val, decimal_places)


@register.filter(name='currencyf')
def format_currency(val):
    return formatter.price(val)


@register.filter(name='datef')
def date_format(date: datetime):
    return formatter.date_format(date)


@register.filter(name='datetimef')
def date_time_format(date_time: datetime):
    return formatter.date_time(date_time)


@register.filter(name='true_if_none')
def true_if_none(value):
    return utils.true_if_none(value)


@register.filter(name='to_boolean')
def to_boolean(value):
    return utils.to_boolean(value)


@register.filter(name='to_hour_minute')
def to_hour_minute(value) -> str:
    return formatter.to_time(value, '%H:%M')


@register.filter(name='formatter_time')
def formatter_time(time_instance):
    return formatter.format_time(time_instance, '%H:%M')
