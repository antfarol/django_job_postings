from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Specialty, Company, Vacancy


def custom_handler404(request, exception):

    return HttpResponseNotFound('<h1>Wrong destination!</h1> \
    <h2>Check your route, please<h/2>')


def custom_handler500(request):

    return HttpResponseServerError()


class MainView(View):

    def get(self, request):

        from django.db.models import Count

        vacancies_spec = Vacancy.objects.values('specialty__code')\
            .annotate(count=Count('company'))
        vacancies_comp = Vacancy.objects.values('company__name')\
            .annotate(count=Count('company'))

        return render(request,
                      'index.html',
                      {'specialties': Specialty.objects.all(),
                       'companies': Company.objects.all(),
                       'vacancies_spec': vacancies_spec,
                       'vacancies_comp': vacancies_comp})


class AllVacanciesView(View):

    def get(self, request):

        return render(request,
                      'vacancies.html',
                      {'vacancies': Vacancy.objects.all()})


class CompaniesListView(View):

    def get(self, request):

        return render(request, 'companies_list.html')


class CompanyView(View):

    def get(self, request, id):

        vacancies = Vacancy.objects.filter(company=id)
        company = Company.objects.get(id=id)

        return render(request, 'company.html',
                      {'vacancies': vacancies,
                       'company': company})


class PostingView(View):

    def get(self, request, id):

        post = Vacancy.objects.get(id=id)

        return render(request, 'posting.html',
                      {'post': post})


class SpecVacanciesView(View):

    def get(self, request, spec):

        vacancies = Vacancy.objects.filter(specialty__code=spec)
        title = Specialty.objects.get(code=spec).title

        return render(request, 'specialisation.html',
                      {'vacancies': vacancies, 'title': title})
