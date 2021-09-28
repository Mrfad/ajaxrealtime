from django.db import models

class SchoolManager(models.Manager):
    def get_by_natural_key(self, sch_name, sch_name1):
        return self.get(sch_name=sch_name, sch_name1=sch_name1)

class School(models.Model):
    sch_name = models.CharField(max_length=1500)
    sch_name1 = models.CharField(max_length=1500)

    objects = SchoolManager()

    class Meta:
        unique_together = [['sch_name', 'sch_name1']]

    def natural_key(self):
        return (self.sch_name, self.sch_name1)

    

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    

    