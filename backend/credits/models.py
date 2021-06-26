""" Credits models. """

# Django
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import EmailField

# Models
from utils.models import BaseModel

class Credit(BaseModel):
    """ Credits model. """

    pending_approval = models.BooleanField(default=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    client = models.ForeignKey(
        'Client', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        related_name='credits')
    


class Client(BaseModel):
    """ Client base model. """

    first_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)

    email = models.EmailField()

    sbs_debt = models.DecimalField(max_digits=10, decimal_places=2)
    
    GOOD = 'good'
    REGULAR = 'regular'
    BAD = 'bad'
    UNKNOWN = 'unknown' 

    DEBTOR_SCORE_CHOICES = [
        (GOOD, 'Bueno'),
        (REGULAR, 'Regular'),
        (BAD, 'Malo'),
        (UNKNOWN, 'Desconocido'),
        
    ]

    debtor_score = models.CharField(
        max_length=7,
        choices=DEBTOR_SCORE_CHOICES,
        default=UNKNOWN,
    )



class CreditApplication(BaseModel):
    """ Credit Application model """

    AI_INDICATOR_CHOICES = [(i,i) for i in range(11)]

    ai_indicator = models.IntegerField(choices=AI_INDICATOR_CHOICES)

    is_approved = models.BooleanField(default=False)

    credit = models.OneToOneField(
        'Credit',
        on_delete=models.CASCADE
    )
