from django.db import models

class Student(models.Model):
    roll=models.CharField( max_length=100)
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField( max_length=200)


def __str__(self):
    return self.name


class Meta:
    db_table = 'sivamcrud'
    verbose_name_plural = 'Student'

    def get_by_id(self, id):
       return Student.objects.get(id=id)