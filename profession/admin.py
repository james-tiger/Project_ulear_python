from django.contrib import admin
from .models import Profession, Vacancy, SalaryByCity, Skill
from django.utils import timezone

# Registering the Profession model
admin.site.register(Profession)

#  Page "General Statistics". The following tab data and graphs should contain the following tab data (there should be provided simultaneously in the form of tables and graphs). All tables and graphs should have the appropriate titles.
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'salary', 'currency', 'posted_date', 'get_skills')
    search_fields = ('title', 'city', 'skills')
    list_filter = ('currency', 'city')

    # Custom method to display the skills as a comma-separated list
    def get_skills(self, obj):
        return ", ".join([skill.skill_name for skill in obj.skills.all()])
    get_skills.short_description = 'Skills'  # Optional: Custom column header for the 'skills' field

# Customizing the SalaryByCity admin page
class SalaryByCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'average_salary')
    search_fields = ('city',)

# Customizing the Skill admin page
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'count')
    search_fields = ('skill_name',)

# Registering the models with the admin site
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(SalaryByCity, SalaryByCityAdmin)
admin.site.register(Skill, SkillAdmin)
