import os
from multiprocessing.connection import Client
from rest_framework.exceptions import ValidationError
import re

# Faqat telefon raqam uchun regex
phone_regex = r'^\+(\d{1,4})[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{1,4}[\s\-]?\d{1,4}[\s\-]?\d{1,4}$'

def check_phone(phone):
    if re.fullmatch(phone_regex, phone):
        return "phone"
    else:
        data = {
            "status": False,
            "message": "Telefon raqamingizni to‘g‘ri kiriting"
        }
        raise ValidationError(data)

def check_user_type(phone):
    if re.fullmatch(phone_regex, phone):
        return "phone"
    else:
        data = {
            "status": False,
            "message": "Telefon raqamingizni to‘g‘ri kiriting"
        }
        raise ValidationError(data)