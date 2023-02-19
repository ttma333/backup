import json
from django import template
from django.template import Library

register = Library()

@register.filter
def tojson(value):
    return json.dumps(value)