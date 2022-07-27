from django.db import models

class StudentInfo(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    sclass = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)


class StudentAcademic(models.Model):
    roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    math = models.IntegerField(null=True, blank=True)
    physic = models.IntegerField(null=True, blank=True)
    chemistry = models.IntegerField(null=True, blank=True)
    english = models.IntegerField(null=True, blank=True)
    biology = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.roll_no.name
<<<<<<< HEAD
class StudentAcademic(models.Model):
    roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    math = models.IntegerField(null=True, blank=True)
    physic = models.IntegerField(null=True, blank=True)
    chemistry = models.IntegerField(null=True, blank=True)
    english = models.IntegerField(null=True, blank=True)
    biology = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.roll_no.name
=======
    
class StudentInfo(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    sclass = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
>>>>>>> 835401ac76b08200f90fcf4577f4dfb78b4c53a2
