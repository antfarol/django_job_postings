from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=60)
    picture = models.CharField(max_length=200,
                               default='https://place-hold.it/100x60')

    def __str__(self) -> str:
        return f'{self.id} {self.title} ({self.code})'


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    logo = models.CharField(max_length=200,
                            default='https://place-hold.it/100x60')
    description = models.CharField(max_length=250)
    employee_count = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.id} {self.name}'


class Vacancy(models.Model):
    title = models.CharField(max_length=60)
    specialty = models.ForeignKey(Specialty,
                                  related_name='vacancies',
                                  on_delete=models.CASCADE)
    company = models.ForeignKey(Company,
                                related_name='vacancies',
                                on_delete=models.CASCADE)
    skills = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self) -> str:
        return f'{self.id} {self.title} ({self.published_at})'
