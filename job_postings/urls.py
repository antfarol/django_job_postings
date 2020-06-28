
from django.contrib import admin
from django.urls import path

from postings.views import MainView, AllVacanciesView, \
    CompanyView, PostingView, SpecVacanciesView, \
    CompaniesListView, custom_handler500, custom_handler404

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies', AllVacanciesView.as_view()),
    path('vacancies/cat/<str:spec>', SpecVacanciesView.as_view()),
    path('vacancies/<int:id>', PostingView.as_view()),
    path('companies', CompaniesListView.as_view()),
    path('companies/<int:id>', CompanyView.as_view()),

]
