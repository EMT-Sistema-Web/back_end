from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from contract.models import Machine

m1 = Machine()
m1.code = 1111
m1.reg_date = datetime(2023, 10, 17, 15, 30)
m1.status = True

def index(request):
    return HttpResponse(m1.code)