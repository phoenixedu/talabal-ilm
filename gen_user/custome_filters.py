from django import template
from datetime import date

register = template.Library()

@register.filter
def calculate_age(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year

    if today.month < date_of_birth.month or (today.month == date_of_birth.month and today.day < date_of_birth.day):
        age -= 1
    if age <= 1:
        sntx = "year"
    else :
        sntx = "years"
    
    return str(f'{age} {sntx}')
