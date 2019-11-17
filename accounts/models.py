from django.db import models
from resource_data.models import Course, Teacher
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """
    A model for all type of users
    """

    is_locked = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=13)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Batch(models.Model):
    """
    It contains information about a class.How many subjects are,
    who are going to teach them,etc.
    """
    branch_sem = models.CharField(max_length=10)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE,)
    teacher_code = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.CharField(max_length=10)
    no_class_week = models.IntegerField()
    no_of_slots = models.IntegerField()


    def __str__(self):
        return str(self.course_code)+' '+str(self.branch_sem)

    class Meta:
        unique_together = (("branch_sem", "course_code"),)
