from django.db import models
from django.utils import timezone

class Skill(models.Model):
    skill_name = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return self.skill_name

class Profession(models.Model):
    name = models.CharField(max_length=100)  # اسم المهنة
    description = models.TextField()  # وصف المهنة
    average_salary = models.FloatField()  # متوسط الراتب
    demand_index = models.IntegerField()  # مؤشر الطلب على المهنة

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100, db_index=True)  # Adding index to city
    salary = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)  # Adding index to salary
    currency = models.CharField(max_length=10, choices=[('RUB', 'RUB'), ('USD', 'USD'), ('EUR', 'EUR')], default='RUB')
    posted_date = models.DateField(default=timezone.now)
    skills = models.ManyToManyField(Skill, related_name='vacancies')  # Correct reference to Skill model

    def __str__(self):
        return self.title

class SalaryByCity(models.Model):
    city = models.CharField(max_length=100)
    average_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.city
