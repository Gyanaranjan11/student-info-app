from django.apps import AppConfig


class StudentinfoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StudentinfoApp'
<<<<<<< HEAD

def test():
    print("_----------------------")
    print("gyana")
    print("_----------------------")
    print("gyana")
=======
class StudentAcademic(models.Model):
    roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    math = models.IntegerField(null=True, blank=True)
    physic = models.IntegerField(null=True, blank=True)
    chemistry = models.IntegerField(null=True, blank=True)
    english = models.IntegerField(null=True, blank=True)
    biology = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.roll_no.name
>>>>>>> 835401ac76b08200f90fcf4577f4dfb78b4c53a2
