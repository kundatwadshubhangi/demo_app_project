from django.shortcuts import render
from django.contrib import messages
from .models import newslatteremail
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader



# Create your views here.
@csrf_exempt 
