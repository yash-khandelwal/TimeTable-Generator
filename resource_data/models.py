from django.db import models
from django.core import validators
# Create your models here.

class Branch(models.Model):
    """
        It contain information about branches.
    """
    branch_code = models.CharField(max_length=10, primary_key=True)
    branch_name = models.CharField(max_length=200)


    def __str__(self):
        return self.branch_code

class Teacher(models.Model):
    """
        This defines the relation table Teacher. It contains required information about teacher.
    """
    teacher_code = models.CharField(max_length=10, primary_key = True)

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    department = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return self.teacher_code

class Course(models.Model):
    """
        It contains the course details.
    """
    course_code = models.CharField(max_length=10, primary_key = True)
    course_name = models.CharField(max_length=200)
    branch_code = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sem = models.IntegerField()
    credits = models.IntegerField(default=3, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])
    lecture = models.IntegerField(default=0, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])
    tutorial = models.IntegerField(default=0, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])
    practical = models.IntegerField(default=0,validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])
    course_intro = models.IntegerField(validators=[validators.MinValueValidator(2010), validators.MaxValueValidator(9999)])

    class Meta:
        ordering = ('sem','course_code')

    def __str__(self):
        return self.course_code

class Room(models.Model):
    room_no = models.CharField(max_length=15,primary_key=True)
    def __str__(self):
        return self.room_no
