from django.db import models
from users.models import User
# Create your models here.

class BoardList(models.Model):
    board_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    school_name = models.CharField(max_length=25)
    reporting_date = models.DateTimeField()
    hit_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board_list'
