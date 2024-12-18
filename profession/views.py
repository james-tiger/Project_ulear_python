from django.shortcuts import render
from .models import Profession, Vacancy, SalaryByCity, Skill
import matplotlib.pyplot as plt
import io
import base64
import requests
from django.utils import timezone

def profession_list(request):
    professions = Profession.objects.all()
    return render(request, 'profession/profession_list.html', {'professions': professions})

def about(request):
    return render(request, 'profession/about.html')

def base(request):
    return render(request, 'base.html')

def get_exchange_rate(currency, date):
    url = f'https://api.exchangerate-api.com/v4/latest/{currency}'
    response = requests.get(url)
    data = response.json()
    if currency != 'RUB':
        return data['rates']['RUB']
    return 1

def statistics(request):
    vacancies = Vacancy.objects.all()

    for vacancy in vacancies:
        if vacancy.salary <= 10000000:
            exchange_rate = get_exchange_rate(vacancy.currency, vacancy.posted_date)
            vacancy.salary_in_rub = vacancy.salary * exchange_rate

    salary_data = {}
    for vacancy in vacancies:
        year = vacancy.posted_date.year
        if year not in salary_data:
            salary_data[year] = []
        salary_data[year].append(vacancy.salary_in_rub)

    years = list(salary_data.keys())
    avg_salaries = [sum(salaries) / len(salaries) for salaries in salary_data.values()]

    fig, ax = plt.subplots()
    ax.plot(years, avg_salaries)
    ax.set(xlabel='Year', ylabel='Average Salary in RUB', title='Salary Dynamics by Year')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

    vacancies_by_year = {}
    for vacancy in vacancies:
        year = vacancy.posted_date.year
        if year not in vacancies_by_year:
            vacancies_by_year[year] = 0
        vacancies_by_year[year] += 1

    vacancy_years = list(vacancies_by_year.keys())
    vacancy_counts = list(vacancies_by_year.values())

    fig2, ax2 = plt.subplots()
    ax2.bar(vacancy_years, vacancy_counts)
    ax2.set(xlabel='Year', ylabel='Number of Vacancies', title='Vacancy Count by Year')

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    img_str2 = base64.b64encode(buffer2.getvalue()).decode('utf-8')

    salary_by_city = {}
    for vacancy in vacancies:
        if vacancy.salary <= 10000000:
            city = vacancy.city
            if city not in salary_by_city:
                salary_by_city[city] = []
            salary_by_city[city].append(vacancy.salary_in_rub)

    sorted_salary_by_city = sorted(salary_by_city.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)

    for city, salaries in sorted_salary_by_city:
        average_salary = sum(salaries) / len(salaries)
        SalaryByCity.objects.update_or_create(city=city, defaults={'average_salary': average_salary})

    skill_counts = {}
    for vacancy in vacancies:
        skills = vacancy.skills.split(',')
        for skill in skills:
            if skill not in skill_counts:
                skill_counts[skill] = 0
            skill_counts[skill] += 1

    top_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)[:20]

    for skill_name, count in top_skills:
        Skill.objects.update_or_create(skill_name=skill_name, defaults={'count': count})

    return render(request, 'profession/statistics.html', {
        'salary_dynamics_chart': img_str,
        'vacancy_count_chart': img_str2,
        'salary_by_city': sorted_salary_by_city,
        'top_skills': top_skills
    })
