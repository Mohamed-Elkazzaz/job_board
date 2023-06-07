from django.db import models

# Create your models here.
JOB_TYPE = (
    ('part time','part time'),
    ('full time','full time'),
)
class Job (models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    # category
    experince = models.IntegerField(default=1)


    def __str__(self) -> str:
        return self.title