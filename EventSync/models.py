from django.db import models

# Create your models here.
class employees_info(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=100, null=False)
    Mob_no=models.CharField(max_length=20, null=False)
    class Meta:
        db_table='employees_info'