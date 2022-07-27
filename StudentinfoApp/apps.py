from django.apps import AppConfig


class StudentinfoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StudentinfoApp'

def test():
    print("_----------------------")
    print("gyana")
    print("_----------------------")
    print("gyana")
class StudentAcademic(models.Model):
    roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    math = models.IntegerField(null=True, blank=True)
    physic = models.IntegerField(null=True, blank=True)
    chemistry = models.IntegerField(null=True, blank=True)
    english = models.IntegerField(null=True, blank=True)
        roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    biology = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.roll_no.name
    
class StudentInfo(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    sclass = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True),roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
class StudentAcademic(models.Model):
    roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    math = models.IntegerField(null=True, blank=True)
    physic = models.IntegerField(null=True, blank=True)
    chemistry = models.IntegerField(null=True, blank=True)
<<<<<<< HEAD
    english = models.IntegerField(null=True, blank=True)
    biology = models.IntegerField(null=True, blank=True)
=======
    english = models.IntegerField(null=True, blank=True),english = models.IntegerField(null=True, blank=True)
    biology = models.IntegerField(null=True, blank=True)
    biology = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.roll_no.name
>>>>>>> ab84f3dbbf94a7e1c965880d9b5466ec941bd48f
