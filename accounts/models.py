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

class Result(models.Model):
    cse1 = models.CharField(blank=True, null=True,max_length=10)
    cse2 = models.CharField(blank=True, null=True,max_length=10)
    cse3 = models.CharField(blank=True, null=True,max_length=10)
    cse4 = models.CharField(blank=True, null=True,max_length=10)
    cse5 = models.CharField(blank=True, null=True,max_length=10)
    cse6 = models.CharField(blank=True, null=True,max_length=10)
    cse7 = models.CharField(blank=True, null=True,max_length=10)
    cse8 = models.CharField(blank=True, null=True,max_length=10)
    ece1 = models.CharField(blank=True, null=True,max_length=10)
    ece2 = models.CharField(blank=True, null=True,max_length=10)
    ece3 = models.CharField(blank=True, null=True,max_length=10)
    ece4 = models.CharField(blank=True, null=True,max_length=10)
    ece5 = models.CharField(blank=True, null=True,max_length=10)
    ece6 = models.CharField(blank=True, null=True,max_length=10)
    ece7 = models.CharField(blank=True, null=True,max_length=10)
    ece8 = models.CharField(blank=True, null=True,max_length=10)
    it1 = models.CharField(blank=True, null=True,max_length=10)
    it2 = models.CharField(blank=True, null=True,max_length=10)
    it3 = models.CharField(blank=True, null=True,max_length=10)
    it4 = models.CharField(blank=True, null=True,max_length=10)
    it5 = models.CharField(blank=True, null=True,max_length=10)
    it6 = models.CharField(blank=True, null=True,max_length=10)
    it7 = models.CharField(blank=True, null=True,max_length=10)
    it8 = models.CharField(blank=True, null=True,max_length=10)


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
