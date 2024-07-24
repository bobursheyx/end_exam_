from django.contrib import admin
from .models import *
from django.db.models import Sum

admin.site.register(Expense)
admin.site.register(Un_Expense)
