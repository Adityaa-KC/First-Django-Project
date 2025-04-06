from django.db import models

class StudentApplication(models.Model):
    COURSE_CHOICES = [
        ('btech', 'B.Tech'),
        ('bba', 'BBA'),
        ('bsc', 'B.Sc'),
        ('ba', 'BA'),
        ('bcom', 'B.Com'),
        ('mba', 'MBA'),
        ('msc', 'M.Sc'),
        ('phd', 'Ph.D'),
    ]

    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    photo = models.ImageField(upload_to='photos/')
    signature = models.ImageField(upload_to='signatures/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
