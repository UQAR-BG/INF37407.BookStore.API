from rest_framework.serializers import ValidationError
import re

def valid_isbn(value):
    regex = "^(?=(?:[^0-9]*[0-9]){10}(?:(?:[^0-9]*[0-9]){3})?$)[\\d-]+$"
    p = re.compile(regex)
    if not (re.search(p, value)):
        raise ValidationError('Le code ISBN ne peut contenir que des chiffres et des tirets.')
    
def isbn_length(value):
    if (len(value) != 13):
        raise ValidationError('Le code ISBN doit faire 13 chiffres de long.')