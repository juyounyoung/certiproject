from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # student_id = models.CharField(max_length=10,null=True, default='')
    account_id = models.CharField(max_length=20, null=False,primary_key=True,  default='', verbose_name="학교이름")
    school_address = models.CharField(max_length=20, null=True, verbose_name = "학교주소")
    # registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

