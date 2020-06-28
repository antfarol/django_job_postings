from data import specialties, companies, jobs
from postings.models import *

for spec in specialties:
    Specialty.objects.create(code=spec['code'], title=spec['title'], picture=spec['pic'])

 for comp in companies:
    Company.objects.create(name=comp['title'], location=comp['location'], description=comp['description'], employee_count=comp['employee_count'])

for job in jobs:
    day=date(int(job['posted'].split('-')[0]), int(job['posted'].split('-')[1]), int(job['posted'].split('-')[2]))
    Vacancy.objects.create(title=job['title'], specialty=Specialty.objects.get(code=job['cat']), company=Company.objects.get(name=job['company']), salary_min=job['salary_from'], salary_max=job['salary_to'], published_at=day, descri
ption=job['desc'])
