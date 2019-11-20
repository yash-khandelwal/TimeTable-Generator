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
    cse1 = models.CharField(blank=True, default='0', null=True,max_length=10)
    cse2 = models.CharField(blank=True, default='0', null=True,max_length=10)
    cse3 = models.CharField(blank=True, default='0', null=True,max_length=10)
    cse4 = models.CharField(blank=True, default='0', null=True,max_length=10)
    cse5 = models.CharField(blank=True, default='0', null=True,max_length=10)
    cse6 = models.CharField(blank=True, default='0', null=True,max_length=10)
    cse7 = models.CharField(blank=True, default='0', null=True,max_length=10)
    cse8 = models.CharField(blank=True, default='0', null=True,max_length=10)
    ece1 = models.CharField(blank=True, default='0', null=True,max_length=10)
    ece2 = models.CharField(blank=True, default='0', null=True,max_length=10)
    ece3 = models.CharField(blank=True, default='0', null=True,max_length=10)
    ece4 = models.CharField(blank=True, default='0', null=True,max_length=10)
    ece5 = models.CharField(blank=True, default='0', null=True,max_length=10)
    ece6 = models.CharField(blank=True, default='0', null=True,max_length=10)
    ece7 = models.CharField(blank=True, default='0', null=True,max_length=10)
    ece8 = models.CharField(blank=True, default='0', null=True,max_length=10)
    it1 = models.CharField(blank=True, default='0', null=True,max_length=10)
    it2 = models.CharField(blank=True, default='0', null=True,max_length=10)
    it3 = models.CharField(blank=True, default='0', null=True,max_length=10)
    it4 = models.CharField(blank=True, default='0', null=True,max_length=10)
    it5 = models.CharField(blank=True, default='0', null=True,max_length=10)
    it6 = models.CharField(blank=True, default='0', null=True,max_length=10)
    it7 = models.CharField(blank=True, default='0', null=True,max_length=10)
    it8 = models.CharField(blank=True, default='0', null=True,max_length=10)

    class Meta:
        ordering = ['id']


class ResultTeacher(models.Model):
    cse1_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    cse2_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    cse3_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    cse4_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    cse5_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    cse6_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    cse7_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    cse8_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    ece1_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    ece2_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    ece3_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    ece4_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    ece5_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    ece6_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    ece7_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    ece8_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    it1_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    it2_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    it3_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    it4_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    it5_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    it6_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    it7_faculty = models.CharField(blank=True, default='', null=True,max_length=10)
    it8_faculty = models.CharField(blank=True, default='', null=True,max_length=10)

    class Meta:
        ordering = ['id']

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
